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
                console.log("error");
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
                    location.href = "/login?next=" + location.href; // 未ログインの場合はログインページへリダイレクト
                }
            }
        })
    }
});

$(function () {
    $(".mark-button").each(function (index, element) {
        const markButton = $(element);
        const markUrl = markButton.attr("data-href");
        $.ajax({
            url: markUrl,
            method: "GET",
            data: {"status": false},
            success: function (data) {
                if (data.marked) {
                    markButton.addClass("mark-button-on");
                }
            }, error: function (error) {
                console.log("error");
            }
        })
    });
});

$(".mark-button").click(function (e) {
    e.preventDefault();
    const markButton = $(this);
    const markCount = markButton.find(".marked-count");
    const markUrl = markButton.attr("data-href");
    if (markUrl) {
        $.ajax({
            url: markUrl,
            method: "GET",
            data: {"status": true}, // いいねが押された場合
            success: function (data) {
                markCount.text(data.markCount);
                if (data.marked) {
                    markButton.addClass("mark-button-on");
                } else {
                    markButton.removeClass("mark-button-on");
                }
            }, error: function (error) {
                console.log("error")
            },
            statusCode: {
                403: function () {
                    location.href = "/login?next=" + location.href; // 未ログインの場合はログインページへリダイレクト
                }
            }
        })
    }
});

$(function () {
    $(".review-button").each(function (index, element) {
        const reviewButton = $(element);
        const reviewUrl = reviewButton.attr("data-href");
        $.ajax({
            url: reviewUrl,
            method: "GET",
            success: function (data) {
                if (data.reviewed) {
                    reviewButton.addClass("review-button-on");
                }
            }, error: function (error) {
                console.log("error");
            }
        })
    });
});

$(function () {
    $(".review-score").each((i, e) => {
        const reviewScore = $(e);
        const score = parseFloat(reviewScore.text());
        if (score >= 4.0) {
        } else if (score >= 3.0) {
            reviewScore.addClass("uk-label-success");
        } else if (score >= 2.0) {
            reviewScore.addClass("uk-label-warning");
        } else {
            reviewScore.addClass("uk-label-danger");
        }
    });
});