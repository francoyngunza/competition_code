window.addEventListener('load', (event) => {
    let input = document.querySelector('input[name=sent_back_amount]');
    input.addEventListener('input', function() {
        this.value = this.value.replace(/[^0-9]/g, '');
    });
});