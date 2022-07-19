$(document).ready(function () {
  function toggleClassMenu() {
    myMenu.classList.add("menu--animatable"), myMenu.classList.contains("menu--visible") ? myMenu.classList.remove("menu--visible") : myMenu.classList.add("menu--visible"), oppMenu.classList.contains("open") ? oppMenu.classList.remove("open") : oppMenu.classList.add("open");
    $('body').toggleClass('body_lock');$('html').toggleClass('body_lock');
  }

  function OnTransitionEnd() {
    myMenu.classList.remove("menu--animatable")
  }

  function OnTransitionEnd() {
    myMenu.classList.remove("menu--animatable")
  }
  var myMenu = document.querySelector(".app-menu"),
    oppMenu = document.querySelector(".open-menu");
  oppMenu.addEventListener("click", toggleClassMenu, !1)

  $('.offers .item').click(function(){
    $(this).toggleClass('offer_active');

  })

  function getWindowWidth() {
    return window.innerWidth || document.body.clientWidth;
  }
  
  if(getWindowWidth() <= 768){

    $('.main-menu li a').click(function(){
      if($(this).siblings().length > 0) {
        $(this).siblings().toggleClass('active-menu-item');
        console.log($(this).siblings());
        return false;
      }
    })
    
  }


  $.fn.scrollToTop = function() {
    $(this).hide().removeAttr("href");
    if ($(window).scrollTop() >= "250") $(this).fadeIn("slow")
    var scrollDiv = $(this);
    $(window).scroll(function() {
     if ($(window).scrollTop() <= "250") $(scrollDiv).fadeOut("slow")
     else $(scrollDiv).fadeIn("slow")
    });
    $(this).click(function() {
     $("html, body").animate({scrollTop: 0}, "slow")
    })
  }

  $("#go-top").scrollToTop();

});

$(document).on("pjax:complete", function () {
  console.log("Done");
});

$(document).on("ready pjax:complete", function () {
  ! function (modules) {
    function __webpack_require__(moduleId) {
      if (installedModules[moduleId]) return installedModules[moduleId].exports;
      var module = installedModules[moduleId] = {
        exports: {},
        id: moduleId,
        loaded: !1
      };
      return modules[moduleId].call(module.exports, module, module.exports, __webpack_require__), module.loaded = !0, module.exports
    }
    var installedModules = {};
    return __webpack_require__.m = modules, __webpack_require__.c = installedModules, __webpack_require__.p = "./static/js/", __webpack_require__(0)
  }([function (module, exports) {
    "use strict";

    function parallaxIt() {
      var $fwindow = $(window),
        scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      $fwindow.on("scroll resize", function () {
        scrollTop = window.pageYOffset || document.documentElement.scrollTop
      }), $('[data-type="content"]').each(function (index, e) {
        var yPos, $contentObj = $(this),
          fgOffset = parseInt($contentObj.offset().top),
          speed = $contentObj.data("speed") || 1;
        $fwindow.on("scroll resize", function () {
          yPos = fgOffset - scrollTop / speed, $contentObj.css("top", yPos)
        })
      }), $('[data-type="background"]').each(function () {
        var yPos, coords, $backgroundObj = $(this),
          bgOffset = parseInt($backgroundObj.offset().top),
          speed = $backgroundObj.data("speed") || 0;
        $fwindow.on("scroll resize", function () {
          yPos = -((scrollTop - bgOffset) / speed), coords = "50% " + yPos + "px", $backgroundObj.css({
            backgroundPosition: coords
          })
        })
      }), $fwindow.trigger("scroll")
    }
    // var top = $(".mainpage .header").offset().top + 150 - parseFloat($(".mainpage .header").css("margin-top").replace(/auto/, 0));
    // $(window).scroll(function (event) {
    //   var y = $(this).scrollTop();
    //   y >= top ? $(".header").removeClass("header-transparent").addClass("header-white") : $(".header").removeClass("header-white").addClass("header-transparent")
    // }), 
    $(".show-more").click(function (e) {
      e.preventDefault();
      var $this = $(this),
        $content = $(this).parents(".dynamic-content-wrap").find(".more-content");
      $($content).toggleClass("hidden"), $(".show-more").toggleClass("up");
      var text = $("span", $this).text();
      $("span", $this).text("Скрыть " == text ? "Показать еще  " : "Скрыть ")
    }), $(".fancybox").fancybox({
      openEffect: "zoom-in-out",
      animationEffect: "zoom-in-out",
      closeEffect: "zoom",
      animationDuration: 766,
      transitionEffect: "fade",
      helpers: {
        overlay: {
          locked: !1
        }
      }
    })
    
    $("#order-form").submit(function (event) {
      event.preventDefault();
      var $this = $(this);
      var form_data = $(this).serialize();
      $('#preloader').fadeIn("slow");
      $.ajax({
        type: "POST",
        url: "send_form.php",
        data: form_data,
        success: function () {
          // alert('Спасибо, Ваш запрос отпрaвлен! Наш менеджер свяжется с Вами в ближайшее время.');
          window.location = "thank-you.html";
        },
        error: function (xhr, str) {
          alert('Возникла ошибка: ' + xhr.responseCode);
        }
      });
      return false; // вырубaeм стaндaртную oтпрaвку фoрмы
    });
    $("#quickform").submit(function (event) {
      event.preventDefault();
      var $this = $(this);
      var form_data = $(this).serialize();
      $('#preloader').fadeIn("slow");
      $.ajax({
        type: "POST",
        url: "send_form.php",
        data: form_data,
        success: function () {
          // alert('Спасибо, Ваш запрос отпрaвлен! Наш менеджер свяжется с Вами в ближайшее время.');
          // $.fancybox.close(true);
          $("#quickform input").val('');
          window.location = "thank-you.html";
        },
        error: function (xhr, str) {
          alert('Возникла ошибка: ' + xhr.responseCode);
        }
      });
      return false; // вырубaeм стaндaртную oтпрaвку фoрмы
    });
    $("#promoform").submit(function (event) {
      event.preventDefault();
      var $this = $(this);
      var form_data = $(this).serialize();
      $('#preloader').fadeIn("slow");
      $.ajax({
        type: "POST",
        url: "send_form.php",
        data: form_data,
        success: function () {
          // alert('Спасибо, Ваш запрос отпрaвлен! Наш менеджер свяжется с Вами в ближайшее время.');
          // $.fancybox.close(true);
          $("#promoform input").val('');
          window.location = "thank-you.html";
        },
        error: function (xhr, str) {
          alert('Возникла ошибка: ' + xhr.responseCode);
        }
      });
      return false; // вырубaeм стaндaртную oтпрaвку фoрмы
    });
    $('#contact-link').click(function () {
      $('#message').show();
      // setTimeout(explode, 4000);
    })
    $('#message .close').click(function () {
      $('#message').hide();
      // setTimeout(explode, 4000);
    })

    // function getCookie(name) {
    //   var matches = document.cookie.match(new RegExp(
    //     "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    //   ));
    //   return matches ? decodeURIComponent(matches[1]) : undefined;
    // }

    // var alertwin = getCookie("alertwin");
    // if (alertwin != "no") {
    //   $(document).mouseleave(function (e) {
    //     if (e.clientY < 0) {
    //       var alertwin = getCookie("alertwin");
    //       if (alertwin != "no") {
    //         $.fancybox.open({
    //           type: 'inline',
    //           src: "#form"
    //         });

    //         var date = new Date;
    //         date.setDate(date.getDate() + 1);
    //         document.cookie = "alertwin=no; path=/; expires=" + date.toUTCString();
    //       }
    //     }
    //   });
    // }
    // =================================================================================
    // cookies
    // =================================================================================
    // $(function() {
    //   // Проверяем запись в куках о посещении
    //   // Если запись есть - ничего не происходит
    //   if (!$.cookie('hideMessage')) {
    //   // если cookie не установлено появится окно с задержкой 5 секунд
    //   var delay_popup = 5000;
    //   setTimeout("document.getElementById('message').style.display='block'", delay_popup);     }
    //      var secs = 600;
    //      var now = new Date();
    //      var exp = new Date(now.getTime() + secs*1000);
    //      $.cookie('hideMessage', true, {
    //    // Время хранения cookie в днях
    //       expires: exp,
    //       path: '/'
    //     });
    // });  
    
    $('.callback-btn  .flex_call a, .callback-btn .flex_what a').click(function(){
        return false;
    }).click(function(){
        $('#preloader').show();
        var link = $(this).attr('href');
        setTimeout(function(){
            location.href = link;
            $('#preloader').hide();
        }, 1000);
    })
    
    
    $.pjax.defaults.timeout = 12000;
    $(document).pjax('a[data-pjax]', '#pjax-container', {
      fragment: '.pjax-container'
    });
    $(document).on('pjax:send', function () {
      $('#preloader').show()
    })
    $(document).on('pjax:complete', function () {
      $('#preloader').hide()
    })

    $('.tabgroup > .tabs-sections').hide();
    $('.tabgroup > div:first-of-type').show();
    $('.tabs-menu ul a').click(function (e) {
      e.preventDefault();
      var $this = $(this),
        tabgroup = '#' + $this.parents('.tabs-menu ul').data('tabgroup'),
        others = $this.closest('li').siblings().children('a'),
        target = $this.attr('href');
      others.removeClass('active');
      $this.addClass('active');
      $(tabgroup).children('div').hide();
      $(target).show();
    })


    var $number = 0;
    var $elements = $('.reviews-wrap .reviews-item');

    function reviewsRandom() {
      $elements.hide();
      $number = Math.floor(Math.random() * $elements.length);
      $elements.eq($number).show();
      return $number + 1;
    };
    reviewsRandom();

    function reviewsNext() {
      $number = $number + 1;
      if ($number == $elements.length) {
        $number = 0;
        $elements.hide();
        $elements.eq($number).show();
      } else {
        $elements.hide();
        $elements.eq($number).show();
      }
    }
    $('.reviews-wrap .update').click(function (e) {
      e.preventDefault();
      setTimeout(reviewsNext, 500);
    })

  }]);

  

  var lazyLoadInstance = new LazyLoad({
    elements_selector: ".lazy"
  });


  function checkPortfolioTab(index) {
    $('.tabs-sections').each(function () {
      $(this).css('display', 'none');
    })
    $('.tabs-menu ul li').each(function () {
      var currentLink = $(this).find('a');
      if (currentLink.hasClass('active')) {
        currentLink.removeClass('active');
      }
      if (currentLink.prop('href').indexOf("#tab"+index) > 0) {
        currentLink.addClass('active');
      }
    })
    $('#tab'+index).css('display', 'block');
  }

  let url = window.location;
  if (url.pathname == "/projects/") {
    if (url.hash) {
      var last = url.hash.substr(-1);
      checkPortfolioTab(last);
    }
    $('a').click(function () {
      if ($(this).prop('href').indexOf("#tab") > 0) {
        var last = $(this).prop('href').substr(-1);
        checkPortfolioTab(last);
      }
    })
  }
})