// // Hide the email input on 'Update Details' page, using opacity to prevent errors once the form is submitted
// function disableEmail() {
//     $("#customer-details-form>#div_id_email>.controls>.emailinput").attr("disabled", true);
// }

// // Remove disabled attribute so that the form can be submitted without throwing errors
// function removeDisableAttrOnSubmit() {
//     $("#customer-details-form").one('submit', (function (e) {
//         e.preventDefault();
//         var $this = $(this);
//         $("#customer-details-form>.full-form>#div_id_email>.controls>.emailinput").attr("disabled", false);
//         $this.submit();
//     }));
// }

// // Call functions 
// $(document).ready(function () {

//     disableEmail();

//     removeDisableAttrOnSubmit();
// });