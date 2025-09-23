// tailwind.config.js
tailwind.config = {
  theme: {
    extend: {
      keyframes: {
        fade: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        wiggle: {
          '0%, 100%': { transform: 'rotate(-3deg)' },
          '50%': { transform: 'rotate(3deg)' },
        },
      },
      animation: {
        fade: 'fade 1s ease-in-out infinite',
        wiggle: 'wiggle 0.5s ease-in-out infinite',
      },
    }
  }
}

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('opacity-100');
    }
  });
});
document.querySelectorAll('[data-observe]').forEach(el => observer.observe(el));