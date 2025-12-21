// Lesson 2 Interactive Scripts

// Initialize AOS (Animate On Scroll)
AOS.init({ duration: 800, offset: 50, once: true });

// Scroll to specific section ID smoothly
function scrollToId(id) {
    const element = document.getElementById(id);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
    }
}

// Toggle visibility of answer sections
// Toggle visibility of answer sections and rotate icon
function toggleAnswer(id) {
    const el = document.getElementById(id);
    const icon = document.getElementById('icon-' + id);

    if (el) {
        if (el.classList.contains('hidden')) {
            el.classList.remove('hidden');
            if (icon) icon.style.transform = 'rotate(180deg)';
        } else {
            el.classList.add('hidden');
            if (icon) icon.style.transform = 'rotate(0deg)';
        }
    }
}

// PDF Download Functionality
function downloadPage() {
    const element = document.getElementById('pdf-content').firstElementChild.cloneNode(true);

    const opt = {
        margin: [0.5, 0.5, 0.5, 0.5], // top, left, bottom, right
        filename: 'George_TOEFL_Lesson2_Handout.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2, useCORS: true, logging: true },
        jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' }
    };

    // Create a temporary container to render the PDF content off-screen
    const container = document.createElement('div');
    container.style.position = 'absolute';
    container.style.left = '-9999px';
    container.style.top = '0';
    container.style.width = '800px'; // Approximate A4 width at 96 DPI
    container.appendChild(element);
    document.body.appendChild(container);

    html2pdf().set(opt).from(element).save().then(() => {
        document.body.removeChild(container);
    }).catch(err => {
        console.error("PDF Generation Error:", err);
        alert('PDF生成失败，请检查网络或稍后重试');
        document.body.removeChild(container); // Ensure cleanup even on error
    });
}
