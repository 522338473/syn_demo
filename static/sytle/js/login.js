$(".validCode_img").click(function () {
    this.src += "?";
});
$("input").focus(function () {
    if ($(this).val() == "") {
        $(this).next().addClass("hide")
    }
});
$("input").blur(function () {
    if ($(this).val() == "") {
        $(this).next().removeClass("hide")
    }
});




var that = this;
    $("#validCode_img").click(function () {
        // {# 图片验证码在线校验 #}
        $.ajax({
            url: "/app01/get_ajax/",
            data: {},
            success: function (data) {
                $("#validCode_img").blur(function () {
                    var msg = $("#validCode_img").val()
                    console.log(msg)
                    console.log(data)
                    if (msg == data) {
                        console.log("验证码校验通过")
                        $("#valid_img").addClass("hide")
                    } else {
                        $("#valid_img").removeClass("hide")
                    }
                })
            }
        })
    })


    $("#code").on("click",function () {
        $("#msg_valid").val($("#telphone").val())
    })


    $("#next_page_one").click(
        function () {
            if (!$("#telphone").val()) {
                $("span").removeClass("hide")
            } else {
                if ($("#page_one span").hasClass("hide")) {
                    console.log("表单第一次验证通过")
                    $("#next_page_one").attr("disabled",false)
                    $("#page_one").addClass("hide").next().removeClass("hide")
                } else {
                    $("#next_page_one").attr("disabled",true)
                }
            }

        }
    )

    $("#next_page_two").click(function () {
        if (!($("#id_number").val() && $("#telphone").val() && $("#address").val())){
            console.log("请填写相关数据")
        } else {
            $("#page_two").addClass("hide").next().removeClass("hide")
        }
    })
