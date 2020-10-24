# Ansible
- Configuration management and provision tool.
- Uses SSH to communicate

## Installation
- Ansible needs to be installed on a control node.
- Tasks can be run off of any machine Ansible is installed on.
- We can even run Ansible from any server; It can run from your laptop

## Managing Servers
- Ansible has a default inventory file used to define which servers it will be managing. After installation, there's an example one you can reference at /etc/ansible/hosts.

## Running Commands
- Ansible will assume you have SSH access available to your servers, usually based on SSH-Key.
```ansible all -m ping -s -k -u vagrant```
- all - Use all defined servers from the inventory file
- -m ping - Use the "ping" module, which simply runs the ping command and returns the results
- -s - Use "sudo" to run the commands
- -k - Ask for a password rather than use key-based authentication
- -u vagrant - Log into servers using user vagrant

## Modules
- Ansible uses "modules" to accomplish most of its Tasks. Modules can do things like install software, copy files, use templates and much more.
- Modules are the way to use Ansible, as they can use available context ("Facts") in order to determine what actions, if any need to be done to accomplish a Task.
```ansible all -s -m apt -a 'pkg=nginx state=installed update_cache=true'```

## Playbooks
- Playbooks can run multiple Tasks and provide some more advanced functionality that we would miss out on using ad-hoc commands.
- nginx.yml
```
---
- hosts: local
  tasks:
   - name: Install Nginx
     apt: pkg=nginx state=installed update_cache=true
```
```ansible-playbook -s nginx.yml```

## Handlers
- A Handler is exactly the same as a Task (it can do anything a Task can), but it will run when called by another Task. You can think of it as part of an Event system; A Handler will take an action when called by an event it listens fo
- nginx.yml
```
---
- hosts: local
  tasks:
   - name: Install Nginx
     apt: pkg=nginx state=installed update_cache=true
     notify:
      - Start Nginx

  handlers:
   - name: Start Nginx
     service: name=nginx state=started
```
## Roles
- Roles are good for organizing multiple, related Tasks and encapsulating data needed to accomplish those Tasks.
```
rolename
 - files
 - handlers
 - meta
 - templates
 - tasks
 - vars
 ```
 - Within each directory, Ansible will search for and read any Yaml file called main.yml automatically.
 ```
 nginx
 - files
 - - h5bp
 ```
 - handlers/main.yml
 ```
 ---
- name: Start Nginx
  service: name=nginx state=started

- name: Reload Nginx
  service: name=nginx state=reloaded
```
- meta/main.yml
```
---
dependencies:
  - { role: ssl }
```
- template/main.yml JINJA2
```
server {
    # Enforce the use of HTTPS
    listen 80 default_server;
    server_name *.{{ '{{' }} domain {{ '}}'  }};
    return 301 https://{{ '{{' }} domain {{ '}}'  }}$request_uri;
}

server {
    listen 443 default_server ssl;

    root /var/www/{{ '{{' }} domain {{ '}}'  }}/public;
    index index.html index.htm index.php;

    access_log /var/log/nginx/{{ '{{' }} domain {{ '}}'  }}.log;
    error_log  /var/log/nginx/{{ '{{' }} domain {{ '}}'  }}-error.log error;

    server_name {{ '{{' }} domain {{ '}}'  }};

    charset utf-8;

    include h5bp/basic.conf;

    ssl_certificate           {{ '{{' }} ssl_crt {{ '}}' }};
    ssl_certificate_key       {{ '{{' }} ssl_key {{ '}}' }};
    include h5bp/directive-only/ssl.conf;

    location /book {
        return 301 http://book.{{ '{{' }} domain {{ '}}'  }};
    }

    location / {
        try_files $uri $uri/ /index.php$is_args$args;
    }

    location = /favicon.ico { log_not_found off; access_log off; }
    location = /robots.txt  { log_not_found off; access_log off; }

    location ~ \.php$ {
        fastcgi_split_path_info ^(.+\.php)(/.+)$;

        fastcgi_pass unix:/var/run/php5-fpm.sock;
        fastcgi_index index.php;

        include fastcgi_params; # fastcgi.conf for version 1.6.1+
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO       $fastcgi_path_info;
        fastcgi_param ENV production;
    }

    # Nginx status
    # Nginx Plus only
    #location /status {
    #    status;
    #    status_format json;
    #    allow 127.0.0.1;
    #    deny all;
    #}

    location ~ ^/(fpmstatus|fpmping)$ {
        access_log off;
        allow 127.0.0.1;
        deny all;
        include fastcgi_params; # fastcgi.conf for version 1.6.1+
        fastcgi_pass unix:/var/run/php5-fpm.sock;
    }
}
```
- Variables/main.yaml
```
---
domain: serversforhackers.com
ssl_key: /etc/ssl/sfh/sfh.key
ssl_crt: /etc/ssl/sfh/sfh.crt
```
- tasks/main.yaml
```
---
- name: Add Nginx Repository
  apt_repository: repo='ppa:nginx/stable' state=present
  register: ppastable

- name: Install Nginx
  apt: pkg=nginx state=installed update_cache=true
  when: ppastable|success
  register: nginxinstalled
  notify:
    - Start Nginx

- name: Add H5BP Config
  when: nginxinstalled|success
  copy: src=h5bp dest=/etc/nginx owner=root group=root

- name: Disable Default Site
  when: nginxinstalled|success
  file: dest=/etc/nginx/sites-enabled/default state=absent

- name: Add SFH Site Config
  when: nginxinstalled|success
  register: sfhconfig
  template: src=serversforhackers.com.j2 dest=/etc/nginx/sites-available/{{ '{{' }} domain {{ '}}'  }}.conf owner=root group=root

- name: Enable SFH Site Config
  when: sfhconfig|success
  file: src=/etc/nginx/sites-available/{{ '{{' }} domain {{ '}}'  }}.conf dest=/etc/nginx/sites-enabled/{{ '{{' }} domain {{ '}}'  }}.conf state=link

- name: Create Web root
  when: nginxinstalled|success
  file: dest=/var/www/{{ '{{' }} domain {{ '}}'  }}/public mode=775 state=directory owner=www-data group=www-data
  notify:
    - Reload Nginx

- name: Web Root Permissions
  when: nginxinstalled|success
  file: dest=/var/www/{{ '{{' }} domain {{ '}}'  }} mode=775 state=directory owner=www-data group=www-data recurse=yes
  notify:
    - Reload Nginx
```

## Facts
- Before running any Tasks, Ansible will gather information about the system it's provisioning. These are called Facts, and include a wide array of system information such as the number of CPU cores, available ipv4 and ipv6 networks, mounted disks, Linux distribution and more.
```
user www-data www-data;
worker_processes {{ ansible_processor_cores * ansible_processor_count }};
pid /var/run/nginx.pid;

# And other configurations...
```

