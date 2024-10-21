document.getElementById("downloadBtn").addEventListener("click", function() {
    const videoUrl = document.getElementById("videoUrl").value;
    const statusElement = document.getElementById("status");

    if (videoUrl) {
        statusElement.innerText = "Downloading...";
        
        // Send the video URL to the backend
        fetch("http://127.0.0.1:8000/download", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: videoUrl })
        })
        .then(response => response.blob())
        .then(blob => {
            // Create a link element to download the video
            const downloadLink = document.createElement("a");
            const url = window.URL.createObjectURL(blob);
            downloadLink.href = url;
            downloadLink.download = "video.mp4";
            document.body.appendChild(downloadLink);
            downloadLink.click();
            document.body.removeChild(downloadLink);
            statusElement.innerText = "Download complete!";
        })
        .catch(error => {
            console.error("Error downloading video:", error);
            statusElement.innerText = "Error downloading video.";
        });
    } else {
        statusElement.innerText = "Please enter a valid URL.";
    }
});














