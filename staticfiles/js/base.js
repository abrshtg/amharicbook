document.addEventListener('DOMContentLoaded', () => {
   
    document.querySelector('.container').onmouseover = function () {
        this.style.background = 'green';
    }
    document.querySelector('.container').onmouseout = function () {
        this.style.background = 'red';
    }
})