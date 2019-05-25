$(function () {
    $(".like-button").each(function (index, element) {
        const likeButton = $(element);
        const likeUrl = likeButton.attr("data-href");
        $.ajax({
            url: likeUrl,
            method: "GET",
            data: {"status": false},
            success: function (data) {
                if (data.liked) {
                    likeButton.addClass("like-button-on");
                }
            }, error: function (error) {
                console.log("error")
            }
        })
    });
});

$(".like-button").click(function (e) {
    e.preventDefault();
    const likeButton = $(this);
    const likeCount = likeButton.find(".liked-count");
    const likeUrl = likeButton.attr("data-href");
    if (likeUrl) {
        $.ajax({
            url: likeUrl,
            method: "GET",
            data: {"status": true}, // いいねが押された場合
            success: function (data) {
                likeCount.text(data.likeCount);
                if (data.liked) {
                    likeButton.addClass("like-button-on");
                } else {
                    likeButton.removeClass("like-button-on");
                }
            }, error: function (error) {
                console.log("error")
            },
            statusCode: {
                403: function () {
                    location.href = "/login"; // 未ログインの場合はログインページへリダイレクト
                }
            }
        })
    }
});