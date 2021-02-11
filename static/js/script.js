/* Collapse javascript imported from W3Schools, link cited in readme file */
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}

/* Javacript providing functionality to emailjs component */

function sendMail(contactForm) {
	emailjs.send("witcherMail", "mailWitcher", {
			"from_name": contactForm.name.value,
			"from_email": contactForm.emailaddress.value,
			"message": contactForm.message.value
		})
		.then(
			function (response) {
				window.alert("Message Sent");
			},
			function (error) {
				window.alert("Message Failed To Send");
			}
		);
	return false; // To block from loading a new page
}