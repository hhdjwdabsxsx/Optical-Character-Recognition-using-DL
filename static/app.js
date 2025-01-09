// JavaScript for enhanced interactivity

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const fileInput = document.querySelector("input[type='file']");
    const submitButton = document.querySelector("button");
    const message = document.createElement("p");
    message.style.display = "none";
    document.body.appendChild(message);

    // Display a preview of the selected image
    const previewContainer = document.createElement("div");
    previewContainer.classList.add("preview-container");
    const previewImage = document.createElement("img");
    previewImage.classList.add("preview-image");
    previewContainer.appendChild(previewImage);
    fileInput.parentElement.appendChild(previewContainer);

    // Handle file selection
    fileInput.addEventListener("change", () => {
        if (fileInput.files.length) {
            const file = fileInput.files[0];
            message.textContent = `Selected file: ${file.name}`;
            message.style.display = "block";

            // Display preview if the file is an image
            if (file.type.startsWith("image/")) {
                const reader = new FileReader();
                reader.onload = (event) => {
                    previewImage.src = event.target.result;
                    previewContainer.style.display = "block";
                };
                reader.readAsDataURL(file);
            } else {
                previewContainer.style.display = "none";
                alert("Please upload a valid image file.");
            }
        } else {
            message.style.display = "none";
            previewContainer.style.display = "none";
        }
    });

    // Handle form submission
    form.addEventListener("submit", (event) => {
        if (!fileInput.files.length) {
            event.preventDefault();
            alert("Please select a file before uploading.");
        } else {
            submitButton.disabled = true;
            message.textContent = "Uploading... Please wait.";
            message.style.display = "block";
        }
    });
});



