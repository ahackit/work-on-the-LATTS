const template = document.createElement('template');
template.innerHTML = `
<style>
h3 {
    color: coral;
}
</style>
<div class="user-card>
<img/>
<div>
<h3>${this.getAttribute(name)}</h3>
<h3><slot name="email"/></h3>
</div>
    
</div>
`;

class UserCard extends HTMLElement {
  constructor() {
    super();

    this.attachShadow({ mode: 'open' });

    this.shadowRoot.append(template.content.cloneNode(true));
    this.innerHTML = ``;
    this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    this.shadowRoot.querySelector('img').innerText = this.getAttribute(
      'avatar'
    );
  }
}

window.customElements.define('user-card', UserCard);
