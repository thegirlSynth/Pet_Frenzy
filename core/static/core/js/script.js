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
