document.addEventListener('DOMContentLoaded', function() {
    const uploadForms = document.querySelectorAll('.upload-form');

    uploadForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            const fileInput = form.querySelector('input[type="file"]');
            if (!fileInput.value) {
                event.preventDefault();
                alert('Please select a file to upload.');
            }
        });
    });
});
