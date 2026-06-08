// Smooth scroll and navbar effect
window.addEventListener('scroll', () => {
  const nav = document.querySelector('nav');
  
  if (window.scrollY > 50) {
    nav.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.12)';
  } else {
    nav.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.08)';
  }
});

// Button hover effect enhancement
document.querySelectorAll('.btn-primary, .btn-secondary').forEach(btn => {
  btn.addEventListener('mouseenter', () => {
    btn.style.transform = 'translateY(-4px)';
  });
  
  btn.addEventListener('mouseleave', () => {
    btn.style.transform = 'translateY(0)';
  });
});
document.addEventListener("DOMContentLoaded", () => {

    const progressBars =
        document.querySelectorAll(".progress-fill");

    const observer =
        new IntersectionObserver(entries => {

        entries.forEach(entry => {

            if(entry.isIntersecting){

                const bar = entry.target;

                const width =
                    bar.dataset.width;

                bar.style.width = width;
            }

        });

    });

    progressBars.forEach(bar => {
        observer.observe(bar);
    });

});
const form = document.getElementById("contactForm");

if(form){

    form.addEventListener("submit", function(e){

        e.preventDefault();

        alert("Cảm ơn bạn đã liên hệ với tôi!");

        form.reset();

    });

}
