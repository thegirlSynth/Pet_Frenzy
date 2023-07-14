
//Remove from Cart
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

//Add to Wishlist
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
            window.location.reload()
        },
    })
})

//Remove from Wishlist
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
            window.location.reload()
        },
    })
})

//Delete Address
$(".delete-address").click(function () {
    var id = $(this).attr("pid").toString();
    var pt = this;
    $.ajax({
        type: "GET",
        url: "/deleteaddress",
        data: {
            add_id: id
        },
        success: function (data) {
            window.location.reload()
        },
    })
})
