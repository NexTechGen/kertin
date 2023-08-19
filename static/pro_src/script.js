/*const search = document.querySelector(".search-box input"),
	  images = document.querySelectorAll(".image-box");


search.addEventListener("keyup", e =>{
	if (e.key == "Enter"){
		let searchValue = search.value,
			value = searchValue.toLowerCase();

			images.forEach(image => {
				if(value == image.dataset.name){
					return image.style.display = "block";
				}
				image.style.display = "none";
			})

			console.log(value);
	}
	
})

search.addEventListener("keyup", () => {
	if(search.value != "") return;
	images.forEach(image => {
		image.style.display = "block";
	})
})

*/

// Select relevant HTML elements
const filterButtons = document.querySelectorAll("#filter-buttons button");
const filterableCards = document.querySelectorAll("#filterable-cards .image-box");

// Function to filter cards based on filter buttons
const filterCards = (e) => {
    document.querySelector("#filter-buttons .active").classList.remove("active");
    e.target.classList.add("active");

    filterableCards.forEach(card => {
        // show the card if it matches the clicked filter or show all cards if "all" filter is clicked
        if(card.dataset.name === e.target.dataset.filter || e.target.dataset.filter === "all") {
            return card.classList.replace("hide", "show");
        }
        card.classList.add("hide");
    });
}

filterButtons.forEach(button => button.addEventListener("click", filterCards));