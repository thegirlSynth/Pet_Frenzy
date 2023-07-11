//plus cart functionality
$(".plus-cart").click(function () {
    var id = $(this).attr("pid").toString();
    var pt = this.parentNode.children[2];
    console.log("pid = ", id)
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            pet_id: id
        },
        success: function (data) {
            console.log("data = ", data);
            pt.innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("totalamount").innerText = data.totalamount;
        },
    })
})

//minus cart functionality
$(".minus-cart").click(function () {
    var id = $(this).attr("pid").toString();
    var pt = this.parentNode.children[2];
    console.log("pid = ", id)
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            pet_id: id
        },
        success: function (data) {
            console.log("data = ", data);
            pt.innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("totalamount").innerText = data.totalamount;
        },
    })
})

//remove from cart
$(".remove-cart").click(function () {
    var id = $(this).attr("pid").toString();
    var pt = this;
    console.log("pid = ", id)
    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            pet_id: id
        },
        success: function (data) {
            console.log("data = ", data);
            pt.innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("totalamount").innerText = data.totalamount;
            pt.parentNode.parentNode.parentNode.parentNode.remove()
        },
    })
})

$(".plus-wishlist").click(function () {
    var id = $(this).attr("pid").toString();
    var pt = this;
    $.ajax({
        type: "GET",
        url: "/pluswishlist",
        data: {
            pet_id: id
        },
        success: function (data) {
            window.location.href = "http://localhost:8000/pet-details/" + id
        },
    })
})

$(".minus-wishlist").click(function () {
    var id = $(this).attr("pid").toString();
    var pt = this;
    $.ajax({
        type: "GET",
        url: "/minuswishlist",
        data: {
            pet_id: id
        },
        success: function (data) {
            window.location.href = "http://localhost:8000/pet-details/" + id
        },
    })
})
