from bs4 import BeautifulSoup

html_doc = """

<!DOCTYPE html>
<html lang="en-gb">
  <head>
    
  
    <!-- Google Tag Manager -->
    <script src="/cdn-cgi/apps/head/48RKkqbIdm80yyY65Oh8W6Css_s.js"></script><script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-NQNW3CX');</script>
    <!-- End Google Tag Manager -->
  


    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="manifest" href="/manifest.json">
    <link rel="preload" href="/en_GB.all.json" as="fetch" crossorigin>
    <link rel="preload" href="/classifications.all.json" as="fetch" crossorigin type="application/json">
    <!-- Kibble:0.17.4 -->
    <!-- Template:0.0.279 -->

    <link rel="stylesheet" href="//cdn.shift72.com/1.3/s72.ui.css">
    <link rel="stylesheet" href="//cdn.shift72.com/1.3/s72.transactional.css">

    <link rel="stylesheet" href="/styles/main.css">

    <link rel="shortcut icon" href="/images/common/favicon.png" type="image/png">
    <link rel="icon" href="/images/common/favicon.png" type="image/png">
    <link rel="apple-touch-icon" href="/images/common/apple-touch-icon.png">

    <link rel="stylesheet" href="https://unpkg.com/swiper@8.4.7/swiper-bundle.min.css" />
    <script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=default,fetch,String.prototype.repeat" defer></script>
    <script src="//cdn.shift72.com/1.3/s72.core.js" defer></script>
    <script src="//cdn.shift72.com/1.3/s72.ui.js" defer></script>
    
    <script src="//cdn.shift72.com/1.3/s72.transactional.js" defer></script>
    
    <script src="https://js.braintreegateway.com/web/dropin/1.26.1/js/dropin.min.js" defer></script>

    

    

    

    <script src="https://unpkg.com/swiper@8.4.7/swiper-bundle.min.js" defer></script>
    <script src="/scripts/main.js" defer></script>

    
  

  
   
   
  
      
        
    
      

    

      
      
    
  

  

  

  <link rel="canonical" href="https://homecinema.curzon.com/collections/a/" />
  

  
    <title>Watch Films Starting With A Online - Curzon Home Cinema</title>
    <meta property="og:title" content="Watch Films Starting With A Online - Curzon Home Cinema">
  
  <meta property="og:url" content="https://homecinema.curzon.com/collections/a/">

  
    <meta property="og:site_name" content="Curzon">
  

  

  
    
  

  
    <meta property="og:video" content="">
    
    <meta property="og:video:width" content="640" />
    <meta property="og:video:height" content="426" />
    <meta property="og:video:type" content="video/mp4" />
  

  
    
      <meta name="description" content="Watch our collection of films starting with A on Curzon Home Cinema. Select from an impressive list of new and original movies online. Watch now.">
      <meta property="og:description" content="Watch our collection of films starting with A on Curzon Home Cinema. Select from an impressive list of new and original movies online. Watch now.">
    
  

  
    <meta name="keywords" content="vod, on demand, ondemand, video, film, movie, rent, stream, cinema, watch, at home">
  

  



    <script>
      window.addEventListener("DOMContentLoaded", function(){
        s72.cfg(function(){ return s72.i18n.load("en", "/en_GB.all.json"); });
        s72.boot({ config: {"ad_delivery":"internal","admin_allow_publish_override":"true","admin_image_root_path":"https://s72-public-assets-production.s3.amazonaws.com/29glj","admin_item_limits":"true","admin_meta_custom_fields":"true","admin_moviexchange_default_territory":"gb","admin_moviexchange_enabled":"true","admin_show_available_to_date":"true","admin_show_google_settings":"true","admin_validate_meta_licensor":"true","app_identifier_amazon":"com.easeltv.curzon","app_link_android":"https://play.google.com/store/apps/details?id=com.curzonhomecinema.android\u0026hl=en_GB\u0026gl=US","app_link_ios":"https://apps.apple.com/us/app/curzon-home-cinema/id1092146553","base_download_url":"https://indiereign113-a.akamaihd.net","base_url":"https://indiereign113-a.akamaihd.net","bg_image_path":"/posters-and-backdrops/1600x1100","carousel":"v2","carousel_image_path":"/posters-and-backdrops/1600x600","chromecast":"true","classification_image_path":"/posters-and-backdrops/170x70","concurrent_content_access_limit":"2","concurrent_streams_limit":"2","content_device_changes_per_period":"1","content_device_changes_period_days":"30","default_image_type":"landscape","detail_page":"v2","device_user_limit":"5","disable_anonymous_watch_now":"true","encoding_profile_hd":"screenplus_hd","encoding_profile_sd":"screenplus_sd","feature_ads":"true","feature_plans":"true","feature_transactional":"true","geo_check_on_play":"true","google_analytics_id":"G-262GTP76MJ","google_merchant_id":"BCR2DN6TV7XOL4QM","google_tag_manager_id":"GTM-NQNW3CX","header_image_path":"/posters-and-backdrops/1200x422","heartbeat_freq":"60","heartbeat_tolerance":"5","image_root_path":"https://d2gynsnnx1ixn5.cloudfront.net/29glj","in_app_product_stores":"apple, google, amazon","ingestion_manager_version":"3","landscape_poster_path":"/posters-and-backdrops/585x330","licensors":"true","licensors_transactions":"true","live_chat_provider":"vocalcom_production","media_item_caption":"true","media_item_caption_genres_count":"2","perform_cc_country_check":"true","plan_based_prices":"true","player_allow_mobile_drm_content":"true","player_resume":"true","portrait_poster_path":"/posters-and-backdrops/282x422","release_window_prices":"true","release_window_scheduling":"true","rental_duration_minutes":"43200","rental_playback_duration_minutes":"2880","rental_redeem_period":"30","required_dob":"true","required_dob_and_gender":"true","required_gender":"true","search_disabled":"false","seo_site_keywords":"vod, on demand, ondemand, video, film, movie, rent, stream, cinema, watch, at home","seo_site_name":"Curzon","seo_title_suffix":"","signup_dob":"true","signup_dob_and_gender":"true","signup_email_optin":"false","signup_gender":"true","storage_limit_GB":"3000","upload":"true","user_analytics":"true","wishlist_enabled":"true"}, toggles: {"admin_add_external_pages":true,"admin_add_report_streams":true,"admin_bg_image":true,"admin_bundles":true,"admin_carousel_image":true,"admin_delete_meta":false,"admin_journal":true,"admin_moviexchange_search":true,"admin_page_images":true,"admin_recommendation_collections":true,"admin_report_activity":true,"admin_report_engagement":true,"admin_report_streamers":true,"admin_user_delete":true,"admin_user_devices":true,"admin_user_plans":true,"admin_v1":false,"classic_streams_disabled":true,"classifications_enabled":true,"kibble":true,"meta_exclude_default_image_types":true,"plan_items_geoblock":true,"tax_settings":true,"uploader_v2":true,"use_new_license_server":true,"use_queued_email_sender":true,"user_library_v4":true} });
      });
    </script>

    <!-- OneTrust Cookies Consent Notice start for homecinema.curzon.com -->
    <script src="https://cdn.cookielaw.org/consent/92fa0c40-45e2-4e7f-bc5b-35a76328efb5.js" type="text/javascript" charset="UTF-8" defer></script>
    <script type="text/javascript">
    function OptanonWrapper() { }
    </script>
    <!-- OneTrust Cookies Consent Notice end for homecinema.curzon.com -->
  </head>
  <body>
    <s72-cookie-consent></s72-cookie-consent>
    <curzon-ga-tracking></curzon-ga-tracking>

    
  
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NQNW3CX" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->
  


    
<header>
  
	<nav id="topnav" style="">
		<div class="nav-item external">
			<a class="nav-link" href="https://www.curzon.com">Cinemas</a>
		</div>
		<div class="nav-item active">
			<a class="nav-link" href="/">Home Cinema</a>
		</div>
	</nav>

  <div class="search-signin-container">
    <div class="header-mobile-menu">
      
<curzon-mobile-nav></curzon-mobile-nav>

    </div>
    <a class="logo" href="/">
      <svg width="145px" height="25px" viewBox="0 0 300 52" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
        <path fill="white" d="M290.755 1.801L290.755 29.744L257.036 0L257.036 49.581L266.279 49.581L266.279 21.727L299.999 51.429L299.999 1.801L290.755 1.801ZM25.268 0.787C30.83 0.787 35.92 2.413 40.676 5.754L40.676 16.695L38.639 14.976C34.655 11.6 30.432 10.014 25.584 10.014C16.328 10.014 10.11 16.387 10.11 25.868C10.11 34.907 16.298 41.467 24.824 41.467C29.883 41.467 34.404 39.702 38.639 36.069L40.667 34.33L40.667 45.92L40.154 46.288C35.946 49.294 31.117 50.756 25.395 50.756C18.174 50.756 11.883 48.316 7.197 43.698C2.555 39.122 0 32.765 0 25.805C0 18.782 2.51 12.594 7.262 7.911C11.987 3.25 18.135 0.787 25.268 0.787ZM195.904 25.79C195.904 11.984 207.096 0.791 220.904 0.791C234.71 0.791 245.904 11.984 245.904 25.79C245.904 39.598 234.71 50.791 220.904 50.791C207.096 50.791 195.904 39.598 195.904 25.79ZM137.163 16.166C137.163 22.667 132.735 27.886 126.558 29.696L142.1 49.582L130.087 49.582L116.028 30.676L116.028 49.581L106.656 49.581L106.656 1.8L122.688 1.8C131.252 1.8 137.163 8.597 137.163 16.166ZM93.49 31.038L93.49 1.801L83.368 1.801L83.368 31.869C83.368 35.453 82.174 37.633 81.119 38.828C79.783 40.446 77.322 42.063 73.666 42.063C70.01 42.063 67.549 40.446 66.213 38.828C65.159 37.633 63.963 35.453 63.963 31.869L63.963 1.801L53.843 1.801L53.843 31.038C53.843 35.699 54.582 40.433 57.541 44.205C61.092 48.865 67.305 51.306 73.666 51.306C80.027 51.306 86.241 48.865 89.791 44.205C92.75 40.433 93.49 35.699 93.49 31.038ZM188.623 1.801L165.744 40.529L188.465 40.529L188.465 49.581L149.38 49.581L171.937 10.536L152.527 10.536L152.527 1.801L188.623 1.801ZM121.056 22.765L116.028 22.782L116.028 10.544L121.815 10.528C124.536 10.528 127.795 12.466 127.835 16.647C127.795 20.828 124.105 22.765 121.056 22.765ZM220.904 40.928C212.543 40.928 205.766 34.151 205.766 25.79C205.766 17.431 212.543 10.654 220.904 10.654C229.264 10.654 236.041 17.431 236.041 25.79C236.041 34.151 229.264 40.928 220.904 40.928Z" transform="translate(0 -9.1552734E-05)" id="Fill-1" fill-rule="evenodd" stroke="none" />
      </svg>
    </a>
    <div class="header-search-signin">
      <div class="primary-search">
        <curzon-search-form mode="header" results-url="/search.html"></curzon-search-form>
      </div>
      <div class="initials-container">
        <s72-user-anon>
          <curzon-signin-button mode="header"></curzon-signin-button>
        </s72-user-anon>

        <s72-user-known>
          <curzon-initials-badge></curzon-initials-badge>
        </s72-user-known>
      </div>
    </div>
  </div>
  
	
	

	<nav id="secondary-nav">
		
			
			
			

			
				
			
			<a
				class=""
				href="/film/"
				target="_self"
				>Films</a>
		
			
			
			

			
				
			
			<a
				class=""
				href="/collections/"
				target="_self"
				>Seasons</a>
		
			
			
			

			
				
			
			<a
				class=""
				href="/browse/"
				target="_self"
				>Discover</a>
		
			
			
			

			
			<a
				class=""
				href="https://www.curzon.com/journal/"
				target="_blank"
				>Journal</a>
		
			
			
			

			
			<a
				class=""
				href="https://www.curzon.com/membership/membership-sales-page/"
				target="_blank"
				>Membership</a>
		
			
			
			

			
				
			
			<a
				class=""
				href="/collections/curzon-home-cinema-presents/"
				target="_self"
				>Curzon Home Cinema Presents...</a>
		
	</nav>


</header>



    
  <div class="page collection-page">
    <div class="container">
      <div class="meta-detail-title-container">
        <h1 class="meta-detail-title" data-slug="/collection/7462">A</h1>
      </div>
    </div>
    <div class="container meta-detail-description">
        <p></p>
    </div>
    <div class="page-collection-list-container slider-and-film-collection slider-4">
      <div class="page-collection-list-item-wrapper">
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/american-star/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/186986"></s72-playback-progress>
        <s72-availability-status data-slug="/film/186986"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/186986/8ddcc967a3ee5ce6380535dbc144fd54.jpg" alt="American Star" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/186986" data-title="American Star" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/186986"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/186986" data-title="American Star" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          American Star
        </div>
        <s72-availability-label data-slug="/film/186986"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 47Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/186986" data-title="American Star" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/a-chiara/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/152556"></s72-playback-progress>
        <s72-availability-status data-slug="/film/152556"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/152556/5ee6602f1db62ca7fffaeb61308739a3.jpg" alt="A Chiara" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/152556" data-title="A Chiara" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/152556"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/152556" data-title="A Chiara" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          A Chiara
        </div>
        <s72-availability-label data-slug="/film/152556"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 1Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/152556" data-title="A Chiara" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/a-ha-the-movie/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/149259"></s72-playback-progress>
        <s72-availability-status data-slug="/film/149259"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/149259/559fd45e678278c4c77ce8be54067ec2.jpg" alt="a-ha: The Movie" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/149259" data-title="a-ha: The Movie" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/149259"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/149259" data-title="a-ha: The Movie" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          a-ha: The Movie
        </div>
        <s72-availability-label data-slug="/film/149259"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 48Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/149259" data-title="a-ha: The Movie" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/about-endlessness/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80709"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80709"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80709/0993b66e426ef7e57a2f25df28626e71.jpg" alt="About Endlessness" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80709" data-title="About Endlessness" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80709"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80709" data-title="About Endlessness" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          About Endlessness
        </div>
        <s72-availability-label data-slug="/film/80709"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 18Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80709" data-title="About Endlessness" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/the-act-of-killing/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/87543"></s72-playback-progress>
        <s72-availability-status data-slug="/film/87543"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/87543/34e54588ce90deda39f05fea787d6eb3.jpg" alt="The Act Of Killing" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/87543" data-title="The Act Of Killing" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/87543"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/87543" data-title="The Act Of Killing" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          The Act Of Killing
        </div>
        <s72-availability-label data-slug="/film/87543"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 55Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/87543" data-title="The Act Of Killing" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/the-adjuster/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80386"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80386"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80386/90504091f82f78ebffc7ca9e219b1dad.jpg" alt="The Adjuster" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80386" data-title="The Adjuster" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80386"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80386" data-title="The Adjuster" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          The Adjuster
        </div>
        <s72-availability-label data-slug="/film/80386"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 42Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80386" data-title="The Adjuster" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/adoration/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80753"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80753"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80753/54efd31453dbeb8d596bcd2267cbdbbe.jpg" alt="Adoration" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80753" data-title="Adoration" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80753"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80753" data-title="Adoration" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Adoration
        </div>
        <s72-availability-label data-slug="/film/80753"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 41Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80753" data-title="Adoration" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/after-life/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80266"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80266"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80266/7c656e7b54069112e080904b6d24b7f6.jpg" alt="After Life" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80266" data-title="After Life" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80266"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80266" data-title="After Life" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          After Life
        </div>
        <s72-availability-label data-slug="/film/80266"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 59Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80266" data-title="After Life" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/after-love-2021/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/125670"></s72-playback-progress>
        <s72-availability-status data-slug="/film/125670"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/125670/b8eb75d633e7880862ffa4c9c643a726.jpg" alt="After Love (2021)" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/125670" data-title="After Love (2021)" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/125670"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/125670" data-title="After Love (2021)" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          After Love (2021)
        </div>
        <s72-availability-label data-slug="/film/125670"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 30Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/125670" data-title="After Love (2021)" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/after-love-2016/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80497"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80497"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80497/524df95ba4c2824bf2968949d987470e.jpg" alt="After Love (2016)" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80497" data-title="After Love (2016)" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80497"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80497" data-title="After Love (2016)" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          After Love (2016)
        </div>
        <s72-availability-label data-slug="/film/80497"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 40Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80497" data-title="After Love (2016)" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/after-the-storm/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80243"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80243"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80243/99b9208ce45b5957104c41c5dea4907d.jpg" alt="After The Storm" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80243" data-title="After The Storm" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80243"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80243" data-title="After The Storm" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          After The Storm
        </div>
        <s72-availability-label data-slug="/film/80243"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 53Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80243" data-title="After The Storm" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/afire/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/173680"></s72-playback-progress>
        <s72-availability-status data-slug="/film/173680"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/173680/70770bd436cb7ff7e748cc318d43a58b.jpg" alt="Afire" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/173680" data-title="Afire" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/173680"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/173680" data-title="Afire" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Afire
        </div>
        <s72-availability-label data-slug="/film/173680"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 42Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/173680" data-title="Afire" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/aftersun/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/163209"></s72-playback-progress>
        <s72-availability-status data-slug="/film/163209"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/163209/b785365d127ce03350dca36b5b02f53f.jpg" alt="Aftersun" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/163209" data-title="Aftersun" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/163209"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/163209" data-title="Aftersun" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Aftersun
        </div>
        <s72-availability-label data-slug="/film/163209"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 42Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/163209" data-title="Aftersun" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/age-of-uprising-the-legend-of-michael-kohlhaas/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80376"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80376"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80376/c196429b603f6c70056cda2be8adb8a4.jpg" alt="Age Of Uprising: The Legend Of Michael Kohlhaas" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80376" data-title="Age Of Uprising: The Legend Of Michael Kohlhaas" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80376"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80376" data-title="Age Of Uprising: The Legend Of Michael Kohlhaas" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Age Of Uprising: The Legend Of Michael Kohlhaas
        </div>
        <s72-availability-label data-slug="/film/80376"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 2Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80376" data-title="Age Of Uprising: The Legend Of Michael Kohlhaas" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/aguirre-wrath-of-god/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80282"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80282"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80282/2647030cf44996df14aaab731271385f.jpg" alt="Aguirre, Wrath Of God" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80282" data-title="Aguirre, Wrath Of God" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80282"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80282" data-title="Aguirre, Wrath Of God" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Aguirre, Wrath Of God
        </div>
        <s72-availability-label data-slug="/film/80282"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 30Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80282" data-title="Aguirre, Wrath Of God" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/ahead-of-the-curve/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/103481"></s72-playback-progress>
        <s72-availability-status data-slug="/film/103481"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/103481/50b195c3732f719e0f45614085fc4007.jpg" alt="Ahead of the Curve" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/103481" data-title="Ahead of the Curve" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/103481"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/103481" data-title="Ahead of the Curve" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Ahead of the Curve
        </div>
        <s72-availability-label data-slug="/film/103481"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 38Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/103481" data-title="Ahead of the Curve" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/ai-weiwei-never-sorry/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80355"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80355"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80355/4895b95e72c0ef2fdfc3c2a573e42c65.jpg" alt="Ai Weiwei: Never Sorry" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80355" data-title="Ai Weiwei: Never Sorry" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80355"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80355" data-title="Ai Weiwei: Never Sorry" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Ai Weiwei: Never Sorry
        </div>
        <s72-availability-label data-slug="/film/80355"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 31Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80355" data-title="Ai Weiwei: Never Sorry" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/ailey/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/131740"></s72-playback-progress>
        <s72-availability-status data-slug="/film/131740"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/131740/17f6b495bbe9508d4f8fd69478b24baf.jpg" alt="Ailey " class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/131740" data-title="Ailey " class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/131740"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/131740" data-title="Ailey " class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Ailey 
        </div>
        <s72-availability-label data-slug="/film/131740"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 35Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/131740" data-title="Ailey " class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/albert-r-n/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80303"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80303"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80303/a78f1528fe91ae14acea60ae1c5f5023.jpg" alt="Albert R.N." class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80303" data-title="Albert R.N." class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80303"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80303" data-title="Albert R.N." class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Albert R.N.
        </div>
        <s72-availability-label data-slug="/film/80303"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 29Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80303" data-title="Albert R.N." class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/alcarras/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/166869"></s72-playback-progress>
        <s72-availability-status data-slug="/film/166869"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/166869/79c3ffcec419700e9c095c91ace71cca.jpg" alt="Alcarràs" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/166869" data-title="Alcarràs" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/166869"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/166869" data-title="Alcarràs" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Alcarràs
        </div>
        <s72-availability-label data-slug="/film/166869"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 0Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/166869" data-title="Alcarràs" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/ali-and-ava/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/141833"></s72-playback-progress>
        <s72-availability-status data-slug="/film/141833"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/141833/302f2ebe82b0872a14732eedd9cca7a8.jpg" alt="Ali &amp; Ava" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/141833" data-title="Ali &amp; Ava" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/141833"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/141833" data-title="Ali &amp; Ava" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Ali & Ava
        </div>
        <s72-availability-label data-slug="/film/141833"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 34Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/141833" data-title="Ali &amp; Ava" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/ali-fear-eats-the-soul/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80248"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80248"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80248/6db8840cb10f42e3a30c186c838f2231.jpg" alt="Ali: Fear Eats The Soul" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80248" data-title="Ali: Fear Eats The Soul" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80248"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80248" data-title="Ali: Fear Eats The Soul" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Ali: Fear Eats The Soul
        </div>
        <s72-availability-label data-slug="/film/80248"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 30Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80248" data-title="Ali: Fear Eats The Soul" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/alibi/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80311"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80311"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80311/0d2f3edaa07680a6bd2cebc4997a2a97.jpg" alt="Alibi" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80311" data-title="Alibi" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80311"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80311" data-title="Alibi" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Alibi
        </div>
        <s72-availability-label data-slug="/film/80311"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 30Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80311" data-title="Alibi" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/alice-in-the-cities/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80262"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80262"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80262/5ef90d9b31c709575330f15d8be62acf.jpg" alt="Alice in the Cities" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80262" data-title="Alice in the Cities" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80262"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80262" data-title="Alice in the Cities" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Alice in the Cities
        </div>
        <s72-availability-label data-slug="/film/80262"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 50Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80262" data-title="Alice in the Cities" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/all-about-my-mother/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80775"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80775"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80775/f858529207d3171785a041091ea9695b.jpg" alt="All About My Mother" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80775" data-title="All About My Mother" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80775"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80775" data-title="All About My Mother" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          All About My Mother
        </div>
        <s72-availability-label data-slug="/film/80775"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 37Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80775" data-title="All About My Mother" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/all-is-vanity/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/156173"></s72-playback-progress>
        <s72-availability-status data-slug="/film/156173"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/156173/03fe75240fa670639e6857908ae82f53.png" alt="All Is Vanity" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/156173" data-title="All Is Vanity" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/156173"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/156173" data-title="All Is Vanity" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          All Is Vanity
        </div>
        <s72-availability-label data-slug="/film/156173"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 12Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/156173" data-title="All Is Vanity" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/almost-holy/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80675"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80675"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80675/f3b953301f169956ca6c8ebfdeb55834.jpg" alt="Almost Holy" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80675" data-title="Almost Holy" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80675"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80675" data-title="Almost Holy" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Almost Holy
        </div>
        <s72-availability-label data-slug="/film/80675"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 33Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80675" data-title="Almost Holy" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/alone-in-berlin/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/84415"></s72-playback-progress>
        <s72-availability-status data-slug="/film/84415"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/84415/074a8c17b783609bd1c418bdf3b4317b.jpg" alt="Alone In Berlin" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/84415" data-title="Alone In Berlin" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/84415"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/84415" data-title="Alone In Berlin" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Alone In Berlin
        </div>
        <s72-availability-label data-slug="/film/84415"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 38Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/84415" data-title="Alone In Berlin" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/alps/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80471"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80471"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80471/920bbca3716109a3354340a8a2209aa7.jpg" alt="Alps" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80471" data-title="Alps" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80471"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80471" data-title="Alps" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Alps
        </div>
        <s72-availability-label data-slug="/film/80471"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 33Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80471" data-title="Alps" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/amadeus-directors-cut/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/182238"></s72-playback-progress>
        <s72-availability-status data-slug="/film/182238"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/182238/634080e12dc8b377bc370b2d4eea970d.jpg" alt="Amadeus: Director&#39;s Cut" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/182238" data-title="Amadeus: Director&#39;s Cut" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/182238"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/182238" data-title="Amadeus: Director&#39;s Cut" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Amadeus: Director's Cut
        </div>
        <s72-availability-label data-slug="/film/182238"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">3h 8Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/182238" data-title="Amadeus: Director&#39;s Cut" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/amanda-2020/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80604"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80604"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80604/4f030affd7fa5fb411e4ed65ecd14ee9.jpg" alt="Amanda (2020)" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80604" data-title="Amanda (2020)" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80604"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80604" data-title="Amanda (2020)" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Amanda (2020)
        </div>
        <s72-availability-label data-slug="/film/80604"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 47Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80604" data-title="Amanda (2020)" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/amanda-2023/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/170397"></s72-playback-progress>
        <s72-availability-status data-slug="/film/170397"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/170397/31a6e4b4360a54a0ed12af4175db514e.jpg" alt="Amanda (2023)" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/170397" data-title="Amanda (2023)" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/170397"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/170397" data-title="Amanda (2023)" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Amanda (2023)
        </div>
        <s72-availability-label data-slug="/film/170397"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 34Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/170397" data-title="Amanda (2023)" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/the-american-friend/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80252"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80252"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80252/9e473055995460c5e69c73748538aa92.jpg" alt="The American Friend" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80252" data-title="The American Friend" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80252"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80252" data-title="The American Friend" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          The American Friend
        </div>
        <s72-availability-label data-slug="/film/80252"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 0Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80252" data-title="The American Friend" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/american-psycho/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/84672"></s72-playback-progress>
        <s72-availability-status data-slug="/film/84672"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/84672/9534a8c3383aeb83c9ce2a9bfdaa4c1a.jpg" alt="American Psycho" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/84672" data-title="American Psycho" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/84672"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/84672" data-title="American Psycho" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          American Psycho
        </div>
        <s72-availability-label data-slug="/film/84672"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 42Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/84672" data-title="American Psycho" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/american-woman/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80797"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80797"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80797/58b6fdcec3c6f7a5de486ecac8de1396.jpg" alt="American Woman" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80797" data-title="American Woman" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80797"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80797" data-title="American Woman" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          American Woman
        </div>
        <s72-availability-label data-slug="/film/80797"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 52Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80797" data-title="American Woman" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/amistad/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/164787"></s72-playback-progress>
        <s72-availability-status data-slug="/film/164787"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/164787/a83ef5d140776adf6be0be2bf60c80c1.jpg" alt="Amistad" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/164787" data-title="Amistad" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/164787"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/164787" data-title="Amistad" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Amistad
        </div>
        <s72-availability-label data-slug="/film/164787"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 35Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/164787" data-title="Amistad" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/ammonite/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/89781"></s72-playback-progress>
        <s72-availability-status data-slug="/film/89781"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/89781/9aebeb1610e5e6ebc5e06276898e7dfb.jpg" alt="Ammonite" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/89781" data-title="Ammonite" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/89781"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/89781" data-title="Ammonite" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Ammonite
        </div>
        <s72-availability-label data-slug="/film/89781"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 0Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/89781" data-title="Ammonite" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/amour/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80592"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80592"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80592/c4cc348d3f048735cd56f9e9e2d51188.jpg" alt="Amour" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80592" data-title="Amour" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80592"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80592" data-title="Amour" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Amour
        </div>
        <s72-availability-label data-slug="/film/80592"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 7Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80592" data-title="Amour" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/amour-fou/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/84673"></s72-playback-progress>
        <s72-availability-status data-slug="/film/84673"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/84673/000e7743993ffdebe647401add2b19a2.jpg" alt="Amour Fou" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/84673" data-title="Amour Fou" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/84673"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/84673" data-title="Amour Fou" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Amour Fou
        </div>
        <s72-availability-label data-slug="/film/84673"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 36Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/84673" data-title="Amour Fou" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/amulet/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/133305"></s72-playback-progress>
        <s72-availability-status data-slug="/film/133305"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/133305/580ce0c7cd53a76f31a864a27946de8b.jpg" alt="Amulet" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/133305" data-title="Amulet" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/133305"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/133305" data-title="Amulet" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Amulet
        </div>
        <s72-availability-label data-slug="/film/133305"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 39Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/133305" data-title="Amulet" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/anatomy-of-a-fall/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/184071"></s72-playback-progress>
        <s72-availability-status data-slug="/film/184071"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/184071/51e0c0a9b4ce6619abf8f7562346d35c.jpg" alt="Anatomy of a Fall" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/184071" data-title="Anatomy of a Fall" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/184071"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/184071" data-title="Anatomy of a Fall" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Anatomy of a Fall
        </div>
        <s72-availability-label data-slug="/film/184071"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 32Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/184071" data-title="Anatomy of a Fall" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/anchorage/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/176565"></s72-playback-progress>
        <s72-availability-status data-slug="/film/176565"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/176565/8ecd3e530b34bd422eb0501909f284e8.jpg" alt="Anchorage" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/176565" data-title="Anchorage" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/176565"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/176565" data-title="Anchorage" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Anchorage
        </div>
        <s72-availability-label data-slug="/film/176565"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 22Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/176565" data-title="Anchorage" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/an-angel-at-my-table/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/125668"></s72-playback-progress>
        <s72-availability-status data-slug="/film/125668"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/125668/e3339f39df80325d572efdbd84b82123.png" alt="An Angel At My Table" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/125668" data-title="An Angel At My Table" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/125668"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/125668" data-title="An Angel At My Table" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          An Angel At My Table
        </div>
        <s72-availability-label data-slug="/film/125668"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 38Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/125668" data-title="An Angel At My Table" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/angelheaded-hipster-the-songs-of-marc-bolan-and-t-rex/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/177388"></s72-playback-progress>
        <s72-availability-status data-slug="/film/177388"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/177388/6934256b1bc7288c0f33b0c3473bbb80.jpg" alt="Angelheaded Hipster: The Songs of Marc Bolan &amp; T. Rex" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/177388" data-title="Angelheaded Hipster: The Songs of Marc Bolan &amp; T. Rex" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/177388"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/177388" data-title="Angelheaded Hipster: The Songs of Marc Bolan &amp; T. Rex" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Angelheaded Hipster: The Songs of Marc Bolan & T. Rex
        </div>
        <s72-availability-label data-slug="/film/177388"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 39Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/177388" data-title="Angelheaded Hipster: The Songs of Marc Bolan &amp; T. Rex" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/an-impossible-love/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80403"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80403"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80403/7c1c1fc4b61665947b20d722835bb590.jpg" alt="An Impossible Love" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80403" data-title="An Impossible Love" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80403"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80403" data-title="An Impossible Love" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          An Impossible Love
        </div>
        <s72-availability-label data-slug="/film/80403"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 10Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80403" data-title="An Impossible Love" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/anais-in-love/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/150778"></s72-playback-progress>
        <s72-availability-status data-slug="/film/150778"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/150778/e861a215c01aed4c3a202c2ecebcca98.png" alt="Anaïs in Love" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/150778" data-title="Anaïs in Love" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/150778"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/150778" data-title="Anaïs in Love" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Anaïs in Love
        </div>
        <s72-availability-label data-slug="/film/150778"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 38Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/150778" data-title="Anaïs in Love" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/and-the-pursuit-of-happiness/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80562"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80562"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80562/0cb023bd2cb98cdaf3d61f874eb567f8.jpg" alt="And The Pursuit Of Happiness" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80562" data-title="And The Pursuit Of Happiness" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80562"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80562" data-title="And The Pursuit Of Happiness" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          And The Pursuit Of Happiness
        </div>
        <s72-availability-label data-slug="/film/80562"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 18Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80562" data-title="And The Pursuit Of Happiness" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/and-then-we-danced/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/84676"></s72-playback-progress>
        <s72-availability-status data-slug="/film/84676"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/84676/7e82ee72e6a3a812640f383c19291bcb.jpg" alt="And Then We Danced" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/84676" data-title="And Then We Danced" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/84676"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/84676" data-title="And Then We Danced" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          And Then We Danced
        </div>
        <s72-availability-label data-slug="/film/84676"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 53Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/84676" data-title="And Then We Danced" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/andrei-rublev/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80361"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80361"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80361/d7790126ee80077686e2c7287d339dfe.jpg" alt="Andrei Rublev" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80361" data-title="Andrei Rublev" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80361"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80361" data-title="Andrei Rublev" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Andrei Rublev
        </div>
        <s72-availability-label data-slug="/film/80361"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 54Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80361" data-title="Andrei Rublev" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/angels-of-evil/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80602"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80602"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80602/35a3246af7c9da6f55ef04611955ea09.jpg" alt="Angels Of Evil" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80602" data-title="Angels Of Evil" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80602"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80602" data-title="Angels Of Evil" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Angels Of Evil
        </div>
        <s72-availability-label data-slug="/film/80602"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 5Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80602" data-title="Angels Of Evil" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/animals/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/84678"></s72-playback-progress>
        <s72-availability-status data-slug="/film/84678"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/84678/ae408e1d9a452762c8efa26848d23861.jpg" alt="Animals" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/84678" data-title="Animals" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/84678"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/84678" data-title="Animals" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Animals
        </div>
        <s72-availability-label data-slug="/film/84678"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 49Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/84678" data-title="Animals" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/anomalisa/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80443"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80443"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80443/02bd5bbd7b3a95c5a58e887c838bba87.jpg" alt="Anomalisa" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80443" data-title="Anomalisa" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80443"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80443" data-title="Anomalisa" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Anomalisa
        </div>
        <s72-availability-label data-slug="/film/80443"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 30Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80443" data-title="Anomalisa" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/anonymous-club/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/163108"></s72-playback-progress>
        <s72-availability-status data-slug="/film/163108"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/163108/d9540ce6711e85ca658dd6269a6a5ca7.jpg" alt="Anonymous Club" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/163108" data-title="Anonymous Club" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/163108"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/163108" data-title="Anonymous Club" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Anonymous Club
        </div>
        <s72-availability-label data-slug="/film/163108"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 26Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/163108" data-title="Anonymous Club" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/another-mans-poison/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80307"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80307"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80307/920d6c72e8b397e2fd01361a7bb9179e.jpg" alt="Another Man&#39;s Poison" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80307" data-title="Another Man&#39;s Poison" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80307"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80307" data-title="Another Man&#39;s Poison" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Another Man's Poison
        </div>
        <s72-availability-label data-slug="/film/80307"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 30Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80307" data-title="Another Man&#39;s Poison" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/another-round/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/101947"></s72-playback-progress>
        <s72-availability-status data-slug="/film/101947"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/101947/9edda76f510569e556a9d3e9cd478e5a.jpg" alt="Another Round" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/101947" data-title="Another Round" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/101947"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/101947" data-title="Another Round" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Another Round
        </div>
        <s72-availability-label data-slug="/film/101947"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 56Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/101947" data-title="Another Round" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/anselm/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/176394"></s72-playback-progress>
        <s72-availability-status data-slug="/film/176394"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/176394/b3652831fb7de0ad2c9a8b5b65741916.jpg" alt="Anselm" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/176394" data-title="Anselm" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/176394"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/176394" data-title="Anselm" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Anselm
        </div>
        <s72-availability-label data-slug="/film/176394"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 33Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/176394" data-title="Anselm" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/antichrist/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80529"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80529"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80529/08b1a8ba2c867bf3edaf12c88d86288c.jpg" alt="Antichrist" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80529" data-title="Antichrist" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80529"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80529" data-title="Antichrist" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Antichrist
        </div>
        <s72-availability-label data-slug="/film/80529"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 48Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80529" data-title="Antichrist" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/apostasy/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80432"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80432"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80432/d68e7e878737fe62357f271f3dfb7b4d.jpg" alt="Apostasy" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80432" data-title="Apostasy" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80432"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80432" data-title="Apostasy" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Apostasy
        </div>
        <s72-availability-label data-slug="/film/80432"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 30Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80432" data-title="Apostasy" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/apples/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/89069"></s72-playback-progress>
        <s72-availability-status data-slug="/film/89069"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/89069/63faf44619a9459d707e0500f1604f71.jpg" alt="Apples" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/89069" data-title="Apples" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/89069"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/89069" data-title="Apples" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Apples
        </div>
        <s72-availability-label data-slug="/film/89069"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 31Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/89069" data-title="Apples" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/appropriate-behaviour/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/84682"></s72-playback-progress>
        <s72-availability-status data-slug="/film/84682"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/84682/8223353b0cc2fd01dea1b31531db32f6.jpg" alt="Appropriate Behaviour" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/84682" data-title="Appropriate Behaviour" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/84682"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/84682" data-title="Appropriate Behaviour" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Appropriate Behaviour
        </div>
        <s72-availability-label data-slug="/film/84682"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 26Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/84682" data-title="Appropriate Behaviour" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/archipelago/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80501"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80501"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80501/53b136d2bfc3942ae1ebe606eb783d90.jpg" alt="Archipelago" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80501" data-title="Archipelago" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80501"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80501" data-title="Archipelago" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Archipelago
        </div>
        <s72-availability-label data-slug="/film/80501"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 54Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80501" data-title="Archipelago" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/ariel/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80336"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80336"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80336/37c111e61fbff2181eadac4bd6bb923b.jpg" alt="Ariel" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80336" data-title="Ariel" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80336"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80336" data-title="Ariel" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Ariel
        </div>
        <s72-availability-label data-slug="/film/80336"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 13Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80336" data-title="Ariel" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/arkansas/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/84685"></s72-playback-progress>
        <s72-availability-status data-slug="/film/84685"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/84685/f3807a17dc0420f95920f15edb30f626.jpg" alt="Arkansas" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/84685" data-title="Arkansas" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/84685"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/84685" data-title="Arkansas" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Arkansas
        </div>
        <s72-availability-label data-slug="/film/84685"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 55Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/84685" data-title="Arkansas" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/armstrong/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/84687"></s72-playback-progress>
        <s72-availability-status data-slug="/film/84687"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/84687/9c8add5ef139e03cdd81051c01440fc0.jpg" alt="Armstrong" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/84687" data-title="Armstrong" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/84687"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/84687" data-title="Armstrong" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Armstrong
        </div>
        <s72-availability-label data-slug="/film/84687"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 40Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/84687" data-title="Armstrong" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/the-artists-wife/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/94042"></s72-playback-progress>
        <s72-availability-status data-slug="/film/94042"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/94042/238312ea5e68e471dfeaf78a14ef427a.jpg" alt="The Artist&#39;s Wife " class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/94042" data-title="The Artist&#39;s Wife " class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/94042"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/94042" data-title="The Artist&#39;s Wife " class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          The Artist's Wife 
        </div>
        <s72-availability-label data-slug="/film/94042"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 34Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/94042" data-title="The Artist&#39;s Wife " class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/ash-is-purest-white/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/87201"></s72-playback-progress>
        <s72-availability-status data-slug="/film/87201"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/87201/493c36a9a116215388a25acab9622ecd.jpg" alt="Ash Is Purest White" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/87201" data-title="Ash Is Purest White" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/87201"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/87201" data-title="Ash Is Purest White" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Ash Is Purest White
        </div>
        <s72-availability-label data-slug="/film/87201"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 15Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/87201" data-title="Ash Is Purest White" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/asia/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80710"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80710"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80710/4eff494b8da2ff6230826fda5191643d.jpg" alt="Asia" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80710" data-title="Asia" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80710"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80710" data-title="Asia" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Asia
        </div>
        <s72-availability-label data-slug="/film/80710"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 25Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80710" data-title="Asia" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/assassins/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/87202"></s72-playback-progress>
        <s72-availability-status data-slug="/film/87202"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/87202/e7ff6bfcd2cb52cf6a8f68e902febfab.jpg" alt="Assassins" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/87202" data-title="Assassins" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/87202"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/87202" data-title="Assassins" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Assassins
        </div>
        <s72-availability-label data-slug="/film/87202"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 44Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/87202" data-title="Assassins" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/the-assistant/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80817"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80817"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80817/8c300bef0619f33fae6c283ab57995ca.jpg" alt="The Assistant" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80817" data-title="The Assistant" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80817"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80817" data-title="The Assistant" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          The Assistant
        </div>
        <s72-availability-label data-slug="/film/80817"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 28Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80817" data-title="The Assistant" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/at-eternitys-gate/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80509"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80509"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80509/ad2a4e183e68c41169564f17eef8d284.jpg" alt="At Eternity&#39;s Gate" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80509" data-title="At Eternity&#39;s Gate" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80509"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80509" data-title="At Eternity&#39;s Gate" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          At Eternity's Gate
        </div>
        <s72-availability-label data-slug="/film/80509"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 51Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80509" data-title="At Eternity&#39;s Gate" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/attenberg/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80380"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80380"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80380/37852b367dd20bedc9618afb56e3e238.jpg" alt="Attenberg" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80380" data-title="Attenberg" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80380"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80380" data-title="Attenberg" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Attenberg
        </div>
        <s72-availability-label data-slug="/film/80380"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 32Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80380" data-title="Attenberg" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/au-revoir-les-enfants/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80546"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80546"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80546/8d49be8dad01346b377f2fa805e1817e.jpg" alt="Au Revoir Les Enfants" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80546" data-title="Au Revoir Les Enfants" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80546"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80546" data-title="Au Revoir Les Enfants" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Au Revoir Les Enfants
        </div>
        <s72-availability-label data-slug="/film/80546"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 44Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80546" data-title="Au Revoir Les Enfants" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/audition/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/84691"></s72-playback-progress>
        <s72-availability-status data-slug="/film/84691"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/84691/36ab6242f3d6c3da80b13e7334f97d29.jpg" alt="Audition" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/84691" data-title="Audition" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/84691"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/84691" data-title="Audition" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Audition
        </div>
        <s72-availability-label data-slug="/film/84691"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 55Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/84691" data-title="Audition" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/the-audition/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/143203"></s72-playback-progress>
        <s72-availability-status data-slug="/film/143203"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/143203/9919de1084c4f868224569ca227a5a59.jpg" alt="The Audition" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/143203" data-title="The Audition" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/143203"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/143203" data-title="The Audition" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          The Audition
        </div>
        <s72-availability-label data-slug="/film/143203"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 39Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/143203" data-title="The Audition" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/the-arbor/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/87547"></s72-playback-progress>
        <s72-availability-status data-slug="/film/87547"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/87547/cfdd3cd9ac62d285b207c022c229c738.jpg" alt="The Arbor" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/87547" data-title="The Arbor" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/87547"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/87547" data-title="The Arbor" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          The Arbor
        </div>
        <s72-availability-label data-slug="/film/87547"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 30Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/87547" data-title="The Arbor" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/the-auschwitz-escape/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/97048"></s72-playback-progress>
        <s72-availability-status data-slug="/film/97048"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/97048/112feecbf7398f58d3a3182e10c754ef.jpg" alt="The Auschwitz Escape" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/97048" data-title="The Auschwitz Escape" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/97048"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/97048" data-title="The Auschwitz Escape" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          The Auschwitz Escape
        </div>
        <s72-availability-label data-slug="/film/97048"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 34Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/97048" data-title="The Auschwitz Escape" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/the-australian-dream/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/87549"></s72-playback-progress>
        <s72-availability-status data-slug="/film/87549"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/87549/a2ea67a567a7d16f97f65ecac6823189.jpg" alt="The Australian Dream" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/87549" data-title="The Australian Dream" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/87549"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/87549" data-title="The Australian Dream" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          The Australian Dream
        </div>
        <s72-availability-label data-slug="/film/87549"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 45Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/87549" data-title="The Australian Dream" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/autobiography-of-a-princess/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80271"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80271"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80271/005303a8352fcd816f3b87f2efa17252.jpg" alt="Autobiography Of A Princess" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80271" data-title="Autobiography Of A Princess" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80271"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80271" data-title="Autobiography Of A Princess" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Autobiography Of A Princess
        </div>
        <s72-availability-label data-slug="/film/80271"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">58Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80271" data-title="Autobiography Of A Princess" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/autumn-almanac/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80391"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80391"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80391/421a3929635b57bfca26a5fa65abcd18.jpg" alt="Autumn Almanac" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80391" data-title="Autumn Almanac" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80391"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80391" data-title="Autumn Almanac" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Autumn Almanac
        </div>
        <s72-availability-label data-slug="/film/80391"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 59Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80391" data-title="Autumn Almanac" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/away/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/87203"></s72-playback-progress>
        <s72-availability-status data-slug="/film/87203"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/87203/7b6031cd1199d6cbde9b2ad53ed9fc62.jpg" alt="Away" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/87203" data-title="Away" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/87203"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/87203" data-title="Away" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Away
        </div>
        <s72-availability-label data-slug="/film/87203"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 15Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/87203" data-title="Away" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/azor/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/127916"></s72-playback-progress>
        <s72-availability-status data-slug="/film/127916"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/127916/e02bec499cade424c783882cd95819b5.jpg" alt="Azor" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/127916" data-title="Azor" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/127916"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/127916" data-title="Azor" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          Azor
        </div>
        <s72-availability-label data-slug="/film/127916"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 40Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/127916" data-title="Azor" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
      </div>
    </div>

  </div>


    

<footer>
  <curzon-member-ribbon href="https://www.curzon.com/membership/membership-sales-page/" text="Become a member"></curzon-member-ribbon>
  <div class="footer-container">
    

  <nav class="bottomnav">

    <div class="footer-nav-main footer-nav-section">
      <ul>
        
          <li><a href="/film/">Films</a> </li>
        
          <li><a href="/collections/">Seasons</a> </li>
        
          <li><a href="/browse/">Discover</a> </li>
        
          <li><a href="https://www.curzon.com/journal/">Journal</a> </li>
        
          <li><a href="https://www.curzon.com/membership/membership-sales-page/">Membership</a> </li>
        
          <li><a href="/collections/curzon-home-cinema-presents/">Curzon Home Cinema Presents...</a> </li>
        
      </ul>
    </div>

    <div class="footer-nav-get-help footer-nav-section">
      <p class="heading">Get help</p>
      <ul>
      
        <li><a href="/help/">Help</a></li>
      
        <li><a href="/terms-and-conditions/">Terms &amp; Conditions</a></li>
      
        <li><a href="/privacy/">Privacy Policy</a></li>
      
      
      </ul>
    </div>

    <div class="footer-nav-my-account footer-nav-section">
      <p class="heading">My account</p>
      <ul>
        <li><a href="https://www.curzon.com/member-account/overview/" target="_blank">Manage account</a></li>
        <li id="footer-signin-button"><curzon-signin-button></curzon-signin-button></li>
      </ul>
    </div>
    <div class="footer-social-newsletter">
      <div class="footer-nav-social">
        <p class="heading">Follow Us</p>
      <ul>
        <li><a href="https://www.instagram.com/curzoncinemas/?hl=en" target="_blank"><i class="s72-icon s72-icon-instagram"></i></a></li>
        <li><a href="https://twitter.com/CurzonCinemas/" target="_blank"><i class="s72-icon s72-icon-twitter"></i></a></li>
        <li><a href="https://www.facebook.com/curzon.cinemas/" target="_blank"><i class="s72-icon s72-icon-facebook"></i></a></li>
      </ul>
      </div>

      <div class="newsletter-form">
        <div class="newsletter-form-heading">Our newsletter</div>
        <curzon-newsletter-signup></curzon-newsletter-signup>
      </div>
    </div>
  </nav>


    <div class="footer-branding">
      <div class="footer-bafta-winner">
        <div class="footer-bafta-winner-heading">Bafta winner 2017</div>
        <div class="footer-bafta-winner-body">Outstanding Contribution <span class="d-md-none"><br /></span>to British Cinema</div>
      </div>

      <div class="footer-notices">
        <div>Curzon © 2021</div>
        <div>All Rights Reserved</div>
        <div><a href="/terms-and-conditions/">Terms &amp; Conditions</a></div>
        <div><a href="/privacy/">Privacy Policy</a></div>
      </div>
    </div>
  </div>
</footer>


    
  
  <script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

    ga('create', 'G-262GTP76MJ', 'auto');
    ga('require', 'ecommerce');
    ga('send', 'pageview');
  </script>
  


    
<!-- Google tag (gtag.js) for AdWords integration -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-350561361"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-350561361');
</script>

  <script defer src="https://static.cloudflareinsights.com/beacon.min.js/v84a3a4012de94ce1a686ba8c167c359c1696973893317" integrity="sha512-euoFGowhlaLqXsPWQ48qSkBSCFs3DPRyiwVu3FjR96cMPx+Fr+gpWRhIafcHwqwCqWS42RZhIudOvEI+Ckf6MA==" data-cf-beacon='{"rayId":"85eb770e985e60fe","version":"2024.2.4","token":"c3a0d1db5bba4fdbac7b06656747c84f"}' crossorigin="anonymous"></script>
</body>
</html>"""


soup = BeautifulSoup(html_doc, 'html.parser')

# Reads the Curzon HTML doc and gets all pieces of text from it
def string_films():
  string = soup.get_text("\n", strip=True)
  print("Films HTML text processed")
  return string


string_films = string_films()

films_list = []


def create_film_list():
  string_line = string_films.split("\n")
  films_list.extend(string_line)
  print("Film list created")
  return string_line
  
  
films_list = create_film_list()
films_list = films_list[10:-21]


"""
def trim_list():
  # Trim extra website info from the list of films
  films_list = films_list[10:-21]
  # print(films_list)
  return films_list


trim_list()
"""

# Create a dictionary containing only film names and lengths
films_dict = {}

def create_film_dict():
  for i in range(0, len(films_list) - 1, 2):
    film_title = films_list[i]
    duration = films_list[i + 1]
    films_dict[film_title] = duration
  print("Film dictionary created")


def print_summary():
  # Print header
  print(f"{'\nFilm title':<40} {'Length'}")
  print('-' * 50)

  # Print films and durations
  for film_title, duration in films_dict.items():
      print(f"{film_title:<40} {duration}")

  # Optional: Print a line to separate the output
  print('-' * 50)

 
create_film_dict()
print_summary()
