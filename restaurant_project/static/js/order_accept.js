document.addEventListener('DOMContentLoaded', function() {
  console.log('order_accept.js loaded');
  const acceptButtons = document.querySelectorAll('.accept-btn');
  acceptButtons.forEach(button => {
    button.addEventListener('click', function() {
      console.log('Accept button clicked');
      const icon = this.querySelector('i');
      const textSpan = this.querySelector('.btn-text');
      if (icon.classList.contains('fa-edit')) {
        icon.classList.remove('fa-edit');
        icon.classList.add('fa-check');
        textSpan.textContent = 'Accepted';
        this.disabled = true;
      }
    });
  });
});
