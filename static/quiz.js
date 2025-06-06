// Medical Quiz Generator JavaScript

document.addEventListener('DOMContentLoaded', function() {
    initializeQuiz();
});

function initializeQuiz() {
    // Initialize specialty selection
    initSpecialtySelection();
    
    // Initialize quiz functionality
    initQuizControls();
    
    // Initialize results page
    initResults();
}

function initSpecialtySelection() {
    const specialtyCards = document.querySelectorAll('.specialty-card');
    
    specialtyCards.forEach(card => {
        card.addEventListener('click', function() {
            const specialty = this.getAttribute('onclick').match(/'([^']+)'/)[1];
            selectSpecialty(specialty);
        });
    });
}

function selectSpecialty(specialty) {
    // Remove selected class from all options
    document.querySelectorAll('.specialty-option').forEach(option => {
        option.classList.remove('selected');
    });
    
    // Add selected class to chosen option
    const selectedInput = document.getElementById(specialty);
    const selectedLabel = document.querySelector(`label[for="${specialty}"]`);
    
    if (selectedInput && selectedLabel) {
        selectedInput.checked = true;
        selectedLabel.classList.add('selected');
    }
}

function initQuizControls() {
    const quizForm = document.getElementById('quizForm');
    
    if (quizForm) {
        // Prevent double submission
        quizForm.addEventListener('submit', function(e) {
            const submitBtn = document.getElementById('submitBtn');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting...';
            }
        });

        // Add keyboard navigation
        document.addEventListener('keydown', function(e) {
            if (e.key >= '1' && e.key <= '4') {
                const optionIndex = parseInt(e.key);
                const option = document.getElementById(`option${optionIndex}`);
                if (option) {
                    option.checked = true;
                    option.dispatchEvent(new Event('change'));
                }
            } else if (e.key === 'Enter') {
                const submitBtn = document.getElementById('submitBtn');
                if (submitBtn && !submitBtn.disabled) {
                    submitBtn.click();
                }
            }
        });
    }
}

function initResults() {
    const resultCards = document.querySelectorAll('.question-review');
    
    // Animate result cards on scroll
    if (resultCards.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateX(0)';
                }
            });
        }, {
            threshold: 0.1
        });

        resultCards.forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateX(-30px)';
            card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(card);
        });
    }

    // Initialize progress bars animation
    animateProgressBars();
}

function animateProgressBars() {
    const progressBars = document.querySelectorAll('.progress-bar');
    
    progressBars.forEach(bar => {
        const targetWidth = bar.style.width;
        bar.style.width = '0%';
        
        setTimeout(() => {
            bar.style.width = targetWidth;
        }, 300);
    });
}

// Utility Functions
function showLoading(element) {
    if (element) {
        element.classList.add('loading');
    }
}

function hideLoading(element) {
    if (element) {
        element.classList.remove('loading');
    }
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

// Performance tracking
function trackQuizPerformance() {
    const startTime = Date.now();
    
    return {
        getElapsedTime: () => {
            return Math.round((Date.now() - startTime) / 1000);
        }
    };
}

// Export functions for global access
window.selectSpecialty = selectSpecialty;
window.showLoading = showLoading;
window.hideLoading = hideLoading;
window.showNotification = showNotification;
