// ... (previous code)

stripe.confirmCardPayment(clientSecret, {
    payment_method: {
        card: card,
    }
}).then(function (result) {
    if (result.error) {
        var errorDiv = document.getElementById('card-errors');
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${result.error.message}</span>`;
        $(errorDiv).html(html);
        $('#payment-form').fadeToggle(100);

        card.update({ 'disabled': false });
        $('#submit-button').attr('disabled', false);
    } else {
        // Check if result.paymentIntent is defined before accessing its properties
        if (result.paymentIntent && result.paymentIntent.status === 'succeeded') {
            form.submit();
        }
    }
}).catch(function (error) {
    console.error("Error confirming card payment:", error);
    // Handle error as needed
    // You might want to display an error message to the user or log the error for debugging
    // Instead of location.reload(), you can handle the error in a way that fits your application
}).finally(function () {
    // Additional code that should run regardless of success or failure
});
