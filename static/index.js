// function displayCardsDynamically(collection1, collection2) {
//     let cardTemplate = document.getElementById("ScoreboardTemplate");

//     db.collection(collection1).get()   //the collection called "products"
//         .then(allproducts => {
//             allproducts.forEach(doc => { //iterate thru each doc
//                 var productCode = doc.data().code;    //get unique ID to each product to be used for fetching right image
//                 var productName = doc.data().name;       // get value of the "name" key
//                 var productStore = doc.data().store;  // get value of the "store" key
//                 var productPrice = doc.data().price;  // get value of the "store" key
//                 var productIngredients = doc.data().ingredients;  // get value of the "details" key
//                 var productTime = doc.data().last_updated;    //get time
//                 var docID = doc.id;
//                 let newcard = cardTemplate.content.cloneNode(true);

//                 //update title and text and image
//                 newcard.querySelector('.card-name').innerHTML = productName;
//                 newcard.querySelector('.card-store').innerHTML = productStore;
//                 newcard.querySelector('.card-price').innerHTML = productPrice;
//                 newcard.querySelector('.card-text').innerHTML = productIngredients;
//                 newcard.querySelector('.card-time').innerHTML = productTime;
//                 newcard.querySelector('.card-image').src = `./images/${productCode}.jpg`; //Example: cake.jpg
//                 newcard.querySelector('a').href = "product.html?docID=" + docID;

//                 //Optional: give unique ids to all elements for future use
//                 // newcard.querySelector('.card-title').setAttribute("id", "ctitle" + i);
//                 // newcard.querySelector('.card-text').setAttribute("id", "ctext" + i);
//                 // newcard.querySelector('.card-image').setAttribute("id", "cimage" + i);

//                 //attach to gallery
//                 document.getElementById(collection + "-go-here").appendChild(newcard);

//                 //i++;   //Optional: iterate variable to serve as unique ID
//             })
//         })
// }

// displayCardsDynamically("players", "scores") 