/* ========================================
   Understanding Deep Learning Tutorial
   Main JavaScript
   ======================================== */

document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initScrollAnimations();
    initTableOfContents();
    initInteractiveDiagrams();
});

/* ========================================
   Navigation
   ======================================== */

function initNavigation() {
    const nav = document.querySelector('.main-nav');
    let lastScroll = 0;
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        // Add/remove background on scroll
        if (currentScroll > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
        
        lastScroll = currentScroll;
    });
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/* ========================================
   Scroll Animations
   ======================================== */

function initScrollAnimations() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    document.querySelectorAll('.feature-card, .chapter-card, .content-section').forEach(el => {
        el.classList.add('animate-on-scroll');
        observer.observe(el);
    });
}

/* ========================================
   Table of Contents (Chapter Pages)
   ======================================== */

function initTableOfContents() {
    const tocLinks = document.querySelectorAll('.toc-list a');
    const sections = document.querySelectorAll('.content-section');
    
    if (tocLinks.length === 0 || sections.length === 0) return;
    
    // Highlight active section on scroll
    const observerOptions = {
        root: null,
        rootMargin: '-20% 0px -70% 0px',
        threshold: 0
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                tocLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);
    
    sections.forEach(section => {
        if (section.id) {
            observer.observe(section);
        }
    });
}

/* ========================================
   Interactive Diagrams
   ======================================== */

function initInteractiveDiagrams() {
    // Initialize any interactive diagrams on the page
    initNeuralNetworkDiagram();
    initActivationFunctionPlot();
    initGradientDescentAnimation();
}

function initNeuralNetworkDiagram() {
    const container = document.getElementById('neural-network-diagram');
    if (!container) return;
    
    const canvas = document.createElement('canvas');
    canvas.width = container.offsetWidth;
    canvas.height = 300;
    container.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    
    // Network configuration
    const layers = [3, 4, 4, 2];
    const layerSpacing = canvas.width / (layers.length + 1);
    const neuronRadius = 15;
    
    // Draw connections
    ctx.strokeStyle = 'rgba(99, 102, 241, 0.2)';
    ctx.lineWidth = 1;
    
    for (let l = 0; l < layers.length - 1; l++) {
        const x1 = layerSpacing * (l + 1);
        const x2 = layerSpacing * (l + 2);
        
        for (let i = 0; i < layers[l]; i++) {
            const y1 = (canvas.height / (layers[l] + 1)) * (i + 1);
            
            for (let j = 0; j < layers[l + 1]; j++) {
                const y2 = (canvas.height / (layers[l + 1] + 1)) * (j + 1);
                
                ctx.beginPath();
                ctx.moveTo(x1, y1);
                ctx.lineTo(x2, y2);
                ctx.stroke();
            }
        }
    }
    
    // Draw neurons
    for (let l = 0; l < layers.length; l++) {
        const x = layerSpacing * (l + 1);
        
        for (let i = 0; i < layers[l]; i++) {
            const y = (canvas.height / (layers[l] + 1)) * (i + 1);
            
            // Glow effect
            const gradient = ctx.createRadialGradient(x, y, 0, x, y, neuronRadius * 2);
            gradient.addColorStop(0, 'rgba(99, 102, 241, 0.3)');
            gradient.addColorStop(1, 'rgba(99, 102, 241, 0)');
            
            ctx.fillStyle = gradient;
            ctx.beginPath();
            ctx.arc(x, y, neuronRadius * 2, 0, Math.PI * 2);
            ctx.fill();
            
            // Neuron circle
            ctx.fillStyle = '#1e1e2a';
            ctx.strokeStyle = '#6366f1';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.arc(x, y, neuronRadius, 0, Math.PI * 2);
            ctx.fill();
            ctx.stroke();
        }
    }
    
    // Labels
    ctx.fillStyle = '#a0a0b0';
    ctx.font = '12px "Space Grotesk", sans-serif';
    ctx.textAlign = 'center';
    
    const labels = ['Input', 'Hidden 1', 'Hidden 2', 'Output'];
    for (let l = 0; l < layers.length; l++) {
        const x = layerSpacing * (l + 1);
        ctx.fillText(labels[l], x, canvas.height - 10);
    }
}

function initActivationFunctionPlot() {
    const container = document.getElementById('activation-plot');
    if (!container) return;
    
    const canvas = document.createElement('canvas');
    canvas.width = container.offsetWidth;
    canvas.height = 250;
    container.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    const centerX = width / 2;
    const centerY = height / 2;
    const scale = 40;
    
    // Draw grid
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
    ctx.lineWidth = 1;
    
    for (let x = 0; x < width; x += scale) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, height);
        ctx.stroke();
    }
    
    for (let y = 0; y < height; y += scale) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(width, y);
        ctx.stroke();
    }
    
    // Draw axes
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
    ctx.lineWidth = 1;
    
    ctx.beginPath();
    ctx.moveTo(0, centerY);
    ctx.lineTo(width, centerY);
    ctx.stroke();
    
    ctx.beginPath();
    ctx.moveTo(centerX, 0);
    ctx.lineTo(centerX, height);
    ctx.stroke();
    
    // Activation functions
    const functions = [
        { name: 'ReLU', color: '#6366f1', fn: x => Math.max(0, x) },
        { name: 'Sigmoid', color: '#22d3ee', fn: x => 1 / (1 + Math.exp(-x)) },
        { name: 'Tanh', color: '#f472b6', fn: x => Math.tanh(x) }
    ];
    
    functions.forEach(({ name, color, fn }) => {
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.beginPath();
        
        for (let px = 0; px < width; px++) {
            const x = (px - centerX) / scale;
            const y = fn(x);
            const py = centerY - y * scale;
            
            if (px === 0) {
                ctx.moveTo(px, py);
            } else {
                ctx.lineTo(px, py);
            }
        }
        
        ctx.stroke();
    });
    
    // Legend
    ctx.font = '11px "Space Grotesk", sans-serif';
    let legendY = 20;
    
    functions.forEach(({ name, color }) => {
        ctx.fillStyle = color;
        ctx.fillRect(10, legendY - 8, 20, 3);
        ctx.fillStyle = '#a0a0b0';
        ctx.textAlign = 'left';
        ctx.fillText(name, 35, legendY);
        legendY += 18;
    });
}

function initGradientDescentAnimation() {
    const container = document.getElementById('gradient-descent-animation');
    if (!container) return;
    
    const canvas = document.createElement('canvas');
    canvas.width = container.offsetWidth;
    canvas.height = 250;
    container.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    // Loss function: simple parabola
    const loss = x => 0.1 * Math.pow(x - width/2, 2) / 100 + 30;
    
    // Draw loss landscape
    ctx.strokeStyle = 'rgba(99, 102, 241, 0.5)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    
    for (let x = 0; x < width; x++) {
        const y = height - loss(x);
        if (x === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
    }
    ctx.stroke();
    
    // Fill under curve
    ctx.lineTo(width, height);
    ctx.lineTo(0, height);
    ctx.closePath();
    
    const gradient = ctx.createLinearGradient(0, 0, 0, height);
    gradient.addColorStop(0, 'rgba(99, 102, 241, 0.1)');
    gradient.addColorStop(1, 'rgba(99, 102, 241, 0)');
    ctx.fillStyle = gradient;
    ctx.fill();
    
    // Animate ball rolling down
    let ballX = 80;
    let velocity = 0;
    const learningRate = 0.02;
    const friction = 0.98;
    
    function animate() {
        // Clear ball area
        ctx.clearRect(0, 0, width, height);
        
        // Redraw curve
        ctx.strokeStyle = 'rgba(99, 102, 241, 0.5)';
        ctx.lineWidth = 2;
        ctx.beginPath();
        
        for (let x = 0; x < width; x++) {
            const y = height - loss(x);
            if (x === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        }
        ctx.stroke();
        
        ctx.lineTo(width, height);
        ctx.lineTo(0, height);
        ctx.closePath();
        ctx.fillStyle = gradient;
        ctx.fill();
        
        // Calculate gradient
        const grad = 0.2 * (ballX - width/2) / 100;
        velocity = velocity * friction - learningRate * grad * 100;
        ballX += velocity;
        
        // Keep ball in bounds
        if (ballX < 20) { ballX = 20; velocity = 0; }
        if (ballX > width - 20) { ballX = width - 20; velocity = 0; }
        
        // Draw ball
        const ballY = height - loss(ballX);
        
        // Glow
        const ballGradient = ctx.createRadialGradient(ballX, ballY, 0, ballX, ballY, 30);
        ballGradient.addColorStop(0, 'rgba(34, 211, 238, 0.4)');
        ballGradient.addColorStop(1, 'rgba(34, 211, 238, 0)');
        ctx.fillStyle = ballGradient;
        ctx.beginPath();
        ctx.arc(ballX, ballY, 30, 0, Math.PI * 2);
        ctx.fill();
        
        // Ball
        ctx.fillStyle = '#22d3ee';
        ctx.beginPath();
        ctx.arc(ballX, ballY, 8, 0, Math.PI * 2);
        ctx.fill();
        
        // Reset if converged
        if (Math.abs(velocity) < 0.01 && Math.abs(ballX - width/2) < 5) {
            setTimeout(() => {
                ballX = Math.random() > 0.5 ? 80 : width - 80;
                velocity = 0;
            }, 2000);
        }
        
        requestAnimationFrame(animate);
    }
    
    animate();
    
    // Labels
    ctx.fillStyle = '#6a6a7a';
    ctx.font = '11px "Space Grotesk", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Parameter θ', width/2, height - 5);
    
    ctx.save();
    ctx.translate(15, height/2);
    ctx.rotate(-Math.PI/2);
    ctx.fillText('Loss L(θ)', 0, 0);
    ctx.restore();
}

/* ========================================
   Utility Functions
   ======================================== */

// Copy code to clipboard
function copyCode(button) {
    const codeBlock = button.closest('.code-block');
    const code = codeBlock.querySelector('code').textContent;
    
    navigator.clipboard.writeText(code).then(() => {
        const originalText = button.textContent;
        button.textContent = 'Copied!';
        setTimeout(() => {
            button.textContent = originalText;
        }, 2000);
    });
}

// Toggle expandable sections
function toggleSection(header) {
    const content = header.nextElementSibling;
    const icon = header.querySelector('.toggle-icon');
    
    content.classList.toggle('expanded');
    icon.classList.toggle('rotated');
}

/* ========================================
   Add animation styles
   ======================================== */

const style = document.createElement('style');
style.textContent = `
    .animate-on-scroll {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }
    
    .animate-on-scroll.visible {
        opacity: 1;
        transform: translateY(0);
    }
    
    .main-nav.scrolled {
        background: rgba(10, 10, 15, 0.95);
    }
`;
document.head.appendChild(style);
