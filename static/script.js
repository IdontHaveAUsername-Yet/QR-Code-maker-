document.getElementById("qrForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const qrData = document.getElementById("qrData").value;

    fetch("/generate_qr", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `qr_data=${encodeURIComponent(qrData)}`,
    })
        .then((response) => {
            if (response.ok) {
                return response.blob();
            } else {
                throw new Error("Error generating QR code.");
            }
        })
        .then((blob) => {
            const qrImage = document.getElementById("qrImage");
            qrImage.src = URL.createObjectURL(blob);
            document.getElementById("qrResult").style.display = "block";
        })
        .catch((error) => console.error(error));
});
