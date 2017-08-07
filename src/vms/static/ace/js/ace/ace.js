/**
 Required. Ace's Basic File to Initiliaze Different Parts & Some Variables.
*/
if( !('ace' in window) ) window['ace'] = {}
if( !('helper' in window['ace']) ) window['ace'].helper = {}
if( !('vars' in window['ace']) ) {
  window['ace'].vars = {
	 'icon'	: ' ace-icon ',
	'.icon'	: '.ace-icon'
  }
}
ace.vars['touch']	= 'ontouchstart' in document.documentElement;


jQuery(function($) {
	//sometimes we try to use 'tap' event instead of 'click' if jquery mobile plugin is available
	ace.click_event = ace.vars['touch'] && $.fn.tap ? 'tap' : 'click';

	//sometimes the only good way to work around browser's pecularities is to detect them using user-agents
	//though it's not accurate
	var agent = navigator.userAgent
	ace.vars['webkit'] = !!agent.match(/AppleWebKit/i)
	ace.vars['safari'] = !!agent.match(/Safari/i) && !agent.match(/Chrome/i);
	ace.vars['android'] = ace.vars['safari'] && !!agent.match(/Android/i)
	ace.vars['ios_safari'] = !!agent.match(/OS ([4-8])(_\d)+ like Mac OS X/i) && !agent.match(/CriOS/i)

	ace.vars['non_auto_fixed'] = ace.vars['android'] || ace.vars['ios_safari'];
	// for android and ios we don't use "top:auto" when breadcrumbs is fixed
	if(ace.vars['non_auto_fixed']) {
		$('body').addClass('mob-safari');
	}

	ace.vars['transition'] = 'transition' in document.body.style || 'WebkitTransition' in document.body.style || 'MozTransition' in document.body.style || 'OTransition' in document.body.style

	/////////////////////////////

	//a list of available functions with their arguments
	// >>> null means enable
	// >>> false means disable
	// >>> array means function arguments
	var available_functions = {
		'general_vars' : null,//general_vars should come first

		'handle_side_menu' : null,
		'add_touch_drag' : null,

		'sidebar_scrollable' : [
							 //true, //enable only if sidebar is fixed , for 2nd approach only
							 true //scroll to selected item? (one time only on page load)
							,true //true = include shortcut buttons in the scrollbars
							,false || ace.vars['safari'] || ace.vars['ios_safari'] //true = include toggle button in the scrollbars
							,200 //> 0 means smooth_scroll, time in ms, used in first approach only, better to be almost the same amount as submenu transition time
							,false//true && ace.vars['touch'] //used in first approach only, true means the scrollbars should be outside of the sidebar
							],

		'sidebar_hoverable' : null,//automatically move up a submenu, if some part of it goes out of window

		'general_things' : null,

		'widget_boxes' : null,
		'widget_reload_handler' : null,

		'settings_box' : null,//settings box
		'settings_rtl' : null,
		'settings_skin' : null,

		'enable_searchbox_autocomplete' : null,

		'auto_hide_sidebar' : null,//disable?
		'auto_padding' : null,//disable
		'auto_container' : null//disable
	};

	//enable these functions with related params
	for(var func_name in available_functions) {
		if(!(func_name in ace)) continue;

		var args = available_functions[func_name];
		if(args === false) continue;//don't run this function

		else if(args == null) args = [jQuery];
		  else if(args instanceof String) args = [jQuery, args];
		    else if(args instanceof Array) args.unshift(jQuery);//prepend jQuery

		ace[func_name].apply(null, args);
	}

})



ace.general_vars = function($) {
	var minimized_menu_class  = 'menu-min';
	var responsive_min_class  = 'responsive-min';
	var horizontal_menu_class = 'h-sidebar';

	var sidebar = $('#sidebar').eq(0);
	//differnet mobile menu styles
	ace.vars['mobile_style'] = 1;//default responsive mode with toggle button inside navbar
	if(sidebar.hasClass('responsive') && !$('#menu-toggler').hasClass('navbar-toggle')) ace.vars['mobile_style'] = 2;//toggle button behind sidebar
	 else if(sidebar.hasClass(responsive_min_class)) ace.vars['mobile_style'] = 3;//minimized menu
	  else if(sidebar.hasClass('navbar-collapse')) ace.vars['mobile_style'] = 4;//collapsible (bootstrap style)

	//update some basic variables
	$(window).on('resize.ace.vars' , function(){
		ace.vars['window'] = {width: parseInt($(this).width()), height: parseInt($(this).height())}
		ace.vars['mobile_view'] = ace.vars['mobile_style'] < 4 && ace.helper.mobile_view();
		ace.vars['collapsible'] = !ace.vars['mobile_view'] && ace.helper.collapsible();
		ace.vars['nav_collapse'] = (ace.vars['collapsible'] || ace.vars['mobile_view']) && $('#navbar').hasClass('navbar-collapse');

		var sidebar = $(document.getElementById('sidebar'));
		ace.vars['minimized'] =
		(!ace.vars['collapsible'] && sidebar.hasClass(minimized_menu_class))
		 ||
		(ace.vars['mobile_style'] == 3 && ace.vars['mobile_view'] && sidebar.hasClass(responsive_min_class))

		ace.vars['horizontal'] = !(ace.vars['mobile_view'] || ace.vars['collapsible']) && sidebar.hasClass(horizontal_menu_class)
	}).triggerHandler('resize.ace.vars');
}

//
ace.general_things = function($) {
	//add scrollbars for user dropdowns
	var has_scroll = !!$.fn.ace_scroll;
	if(has_scroll) $('.dropdown-content').ace_scroll({reset: false, mouseWheelLock: true})
	/**
	//add scrollbars to body
	 if(has_scroll) $('body').ace_scroll({size: ace.helper.winHeight()})
	 $('body').css('position', 'static')
	*/

	//reset scrolls bars on window resize
	$(window).on('resize.reset_scroll', function() {
		/**
		 //reset body scrollbars
		 if(has_scroll) $('body').ace_scroll('update', {size : ace.helper.winHeight()})
		*/
		if(has_scroll) $('.ace-scroll').ace_scroll('reset');
	});
	$(document).on('settings.ace.reset_scroll', function(e, name) {
		if(name == 'sidebar_collapsed' && has_scroll) $('.ace-scroll').ace_scroll('reset');
	});


	//change a dropdown to "dropup" depending on its position
	$(document).on('click.dropdown.pos', '.dropdown-toggle[data-position="auto"]', function() {
		var offset = $(this).offset();
		var parent = $(this.parentNode);

		if ( parseInt(offset.top + $(this).height()) + 50
				>
			(ace.helper.scrollTop() + ace.helper.winHeight() - parent.find('.dropdown-menu').eq(0).height())
			) parent.addClass('dropup');
		else parent.removeClass('dropup');
	});


	//prevent dropdowns from hiding when a tab is selected
	$(document).on('click', '.dropdown-navbar .nav-tabs', function(e){
		e.stopPropagation();
		var $this , href
		var that = e.target
		if( ($this = $(e.target).closest('[data-toggle=tab]')) && $this.length > 0) {
			$this.tab('show');
			e.preventDefault();
		}
	});

	//prevent dropdowns from hiding when a from is clicked
	/**$(document).on('click', '.dropdown-navbar form', function(e){
		e.stopPropagation();
	});*/


	//disable navbar icon animation upon click
	$('.ace-nav [class*="icon-animated-"]').closest('a').one('click', function(){
		var icon = $(this).find('[class*="icon-animated-"]').eq(0);
		var $match = icon.attr('class').match(/icon\-animated\-([\d\w]+)/);
		icon.removeClass($match[0]);
	});


	//tooltip in sidebar items
	$('.sidebar .nav-list .badge[title],.sidebar .nav-list .badge[title]').each(function() {
		var tooltip_class = $(this).attr('class').match(/tooltip\-(?:\w+)/);
		tooltip_class = tooltip_class ? tooltip_class[0] : 'tooltip-error';
		$(this).tooltip({
			'placement': function (context, source) {
				var offset = $(source).offset();

				if( parseInt(offset.left) < parseInt(document.body.scrollWidth / 2) ) return 'right';
				return 'left';
			},
			container: 'body',
			template: '<div class="tooltip '+tooltip_class+'"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>'
		});
	});

	//or something like this if items are dynamically inserted
	/**$('.sidebar').tooltip({
		'placement': function (context, source) {
			var offset = $(source).offset();

			if( parseInt(offset.left) < parseInt(document.body.scrollWidth / 2) ) return 'right';
			return 'left';
		},
		selector: '.nav-list .badge[title],.nav-list .label[title]',
		container: 'body',
		template: '<div class="tooltip tooltip-error"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>'
	});*/




	//the scroll to top button
	var scroll_btn = $('.btn-scroll-up');
	if(scroll_btn.length > 0) {
		var is_visible = false;
		$(window).on('scroll.scroll_btn', function() {
			if(ace.helper.scrollTop() > parseInt(ace.helper.winHeight() / 4)) {
				if(!is_visible) {
					scroll_btn.addClass('display');
					is_visible = true;
				}
			} else {
				if(is_visible) {
					scroll_btn.removeClass('display');
					is_visible = false;
				}
			}
		}).triggerHandler('scroll.scroll_btn');

		scroll_btn.on(ace.click_event, function(){
			var duration = Math.min(500, Math.max(100, parseInt(ace.helper.scrollTop() / 3)));
			$('html,body').animate({scrollTop: 0}, duration);
			return false;
		});
	}


	//chrome and webkit have a problem here when resizing from 460px to more
	//we should force them redraw the navbar!
	if( ace.vars['webkit'] ) {
		var ace_nav = $('.ace-nav').get(0);
		if( ace_nav ) $(window).on('resize.webkit' , function(){
			ace.helper.redraw(ace_nav);
		});
	}

}




//some functions
ace.helper.collapsible = function() {
	var toggle
	return (document.querySelector('#sidebar.navbar-collapse') != null)
	&& ((toggle = document.querySelector('.navbar-toggle[data-target*=".sidebar"]')) != null)
	&&  toggle.scrollHeight > 0
	//sidebar is collapsible and collapse button is visible?
}
ace.helper.mobile_view = function() {
	var toggle
	return ((toggle = document.getElementById('menu-toggler')) != null	&& toggle.scrollHeight > 0)
}

ace.helper.redraw = function(elem) {
	var saved_val = elem.style['display'];
	elem.style.display = 'none';
	elem.offsetHeight;
	elem.style.display = saved_val;
}

ace.helper.scrollTop = function() {
	return document.scrollTop || document.documentElement.scrollTop || document.body.scrollTop
	//return $(window).scrollTop();
}
ace.helper.winHeight = function() {
	return window.innerHeight || document.documentElement.clientHeight;
	//return $(window).innerHeight();
}
ace.helper.camelCase = function(str) {
	return str.replace(/-([\da-z])/gi, function(match, chr) {
	  return chr ? chr.toUpperCase() : '';
	});
}
ace.helper.removeStyle =
  'removeProperty' in document.body.style
  ?
  function(elem, prop) { elem.style.removeProperty(prop) }
  :
  function(elem, prop) { elem.style[ace.helper.camelCase(prop)] = '' }


ace.helper.hasClass =
  'classList' in document.documentElement
  ?
  function(elem, className) { return elem.classList.contains(className); }
  :
  function(elem, className) { return elem.className.indexOf(className) > -1; }
