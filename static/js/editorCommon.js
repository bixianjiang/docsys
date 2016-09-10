$(function() {
	/*个人设置下拉列表*/
	$(".admin-information span").click(function() {
		$(this).siblings(".a-information-cont").toggle()

	})
	$(document).bind("click", function(e) {
			var target = $(e.target);
			if((target.closest(".admin-information").length == 0) && (target.closest(".a-information-cont").length == 0)) {
				$(".a-information-cont").hide();
			}
		})
		/*新建文档下拉列表*/
	$(".new-document span").click(function() {
		$(this).siblings(".new-document-cont").toggle()

	})
	$(document).bind("click", function(e) {
			var target = $(e.target);
			if((target.closest(".new-document").length == 0) && (target.closest(".new-document-cont").length == 0)) {
				$(".new-document-cont").hide();
			}
		})
		/*文档设置*/
	$(".e-document-set").click(function() {
		$(this).siblings(".e-document-set-cont").toggle();
		$(this).parent().siblings().find(".e-document-set-cont").hide();
		$(this).parent().toggleClass("e-list-document-li-hover");
		$(this).parent().siblings().removeClass("e-list-document-li-hover");

	})

	$(document).bind("click", function(e) {
		var target = $(e.target);
		/*修改标题传值保存的代码--开始*/
		var documentTitle = $(".e-list-document-li-hover").find(".e-l-l-title-input").val();
		//alert(documentTitle);
		$(".e-list-document-li-hover").find(".editor-list-li-title").html(documentTitle);
		/*修改标题传值保存的代码--结束*/
		if((target.closest(".e-document-set").length == 0) && (target.closest(".e-document-set-cont").length == 0)) {
			$(".e-document-set-cont").hide();
			$(".e-document-set").parent().removeClass("e-list-document-li-hover");
			
		}
	})

});

/*判断当前页面连接加样式*/
$(document).ready(function() {

	$(".left-navigation li a").each(function() {

		$this = $(this);

		if($this[0].href == String(window.location)) {

			$this.addClass("this-page");

		}

	});

});
/*判断当前页面连接加样式*/

/*弹出的modal层*/
/*背景蒙版*/
$(".modal-bak").click(function() {
		$(".modal-bak").hide();
		$(".invitation-news-user").hide();
		$(".share-files").hide();
		$(".confirm-delete").hide();
			$(".save-document").hide();
	})

	/*关闭叉号*/
$(".i-news-user-close").click(function() {
		$(".modal-bak").hide();
		$(".invitation-news-user").hide();
		$(".share-files").hide();
		$(".confirm-delete").hide();
			$(".save-document").hide();
	})

	/*邀请新用户*/
$("#invitation-news").click(function() {
		$(".modal-bak").show();
		$(".invitation-news-user").show();
	})
		/*提示*/
$(".invitation-success-btn").on("click",function(){
	$(".invitation-success-cont").html("发送成功/失败");
	$(".invitation-success-cont").show();
	$(".invitation-news-user").hide();
	$(".modal-bak").hide();
	setTimeout(function(){
		$(".invitation-success-cont").hide();
	},2000)
})

	/*分享*/
$(".share-files-btn").click(function() {
		$(".modal-bak").show();
		$(".share-files").show();
	})
		/*提示*/
$(".share-success-btn").on("click",function(){
	$(".share-success-cont").html("分享成功/失败");
	$(".share-success-cont").show();
	$(".share-files").hide();
	$(".modal-bak").hide();
	setTimeout(function(){
		$(".share-success-cont").hide();
	},2000)
})

	/*删除*/
$(".confirm-delete-btn").click(function() {
	$(".modal-bak").show();
	$(".confirm-delete").show();
})

	/*删除文档*/
$(".c-delete-this-document").click(function(){
	$(".e-list-document-li-hover").hide();
$(".modal-bak").hide();
	$(".confirm-delete").hide();		
})
		/*提示*/
$(".delete-success-btn").on("click",function(){
	$(".delete-success-cont").html("删除成功/失败");
	$(".delete-success-cont").show();
	$(".confirm-delete").hide();
	$(".modal-bak").hide();
	setTimeout(function(){
		$(".delete-success-cont").hide();
	},2000)
})

	/*文档保存*/
$(".save-document-btn").click(function() {
	$(".modal-bak").show();
	$(".save-document").show();
})
		/*提示*/
$(".save-success-btn").on("click",function(){
	$(".save-success-cont").html("保存成功/失败");
	$(".save-success-cont").show();
	$(".save-document").hide();
	$(".modal-bak").hide();
	setTimeout(function(){
		$(".save-success-cont").hide();
	},2000)
})

