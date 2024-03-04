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

    
  

  
   
   
  
      
        
    
      

    

      
      
    
  

  

  

  <link rel="canonical" href="https://homecinema.curzon.com/collections/0-9/" />
  

  
    <title>Watch 0-9 Collection of Films Online - Curzon Home Cinema</title>
    <meta property="og:title" content="Watch 0-9 Collection of Films Online - Curzon Home Cinema">
  
  <meta property="og:url" content="https://homecinema.curzon.com/collections/0-9/">

  
    <meta property="og:site_name" content="Curzon">
  

  

  
    
  

  
    <meta property="og:video" content="">
    
    <meta property="og:video:width" content="640" />
    <meta property="og:video:height" content="426" />
    <meta property="og:video:type" content="video/mp4" />
  

  
    
      <meta name="description" content="Watch our 0-9 collection of films on Curzon Home Cinema. Choose from a carefully curated list of new and original movies online. Watch now.">
      <meta property="og:description" content="Watch our 0-9 collection of films on Curzon Home Cinema. Choose from a carefully curated list of new and original movies online. Watch now.">
    
  

  
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
        <h1 class="meta-detail-title" data-slug="/collection/7487">0-9</h1>
      </div>
    </div>
    <div class="container meta-detail-description">
        <p></p>
    </div>
    <div class="page-collection-list-container slider-and-film-collection slider-4">
      <div class="page-collection-list-item-wrapper">
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/120-bpm/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80654"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80654"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80654/b896bb4a73ddcb78ed2c480e2775ad9d.jpg" alt="120 BPM" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80654" data-title="120 BPM" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80654"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80654" data-title="120 BPM" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          120 BPM
        </div>
        <s72-availability-label data-slug="/film/80654"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 23Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80654" data-title="120 BPM" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/13-assassins/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80676"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80676"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80676/dd8f672abffd1ee89ad7c4b873f3014e.jpg" alt="13 Assassins" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80676" data-title="13 Assassins" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80676"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80676" data-title="13 Assassins" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          13 Assassins
        </div>
        <s72-availability-label data-slug="/film/80676"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 6Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80676" data-title="13 Assassins" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/1976/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/167492"></s72-playback-progress>
        <s72-availability-status data-slug="/film/167492"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/167492/d61af67b5a18479085c0fb13098d6338.jpg" alt="1976" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/167492" data-title="1976" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/167492"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/167492" data-title="1976" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          1976
        </div>
        <s72-availability-label data-slug="/film/167492"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 35Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/167492" data-title="1976" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/1985/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/84649"></s72-playback-progress>
        <s72-availability-status data-slug="/film/84649"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/84649/d3e9eb02d53ac8e31030877d5734ace2.jpg" alt="1985" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/84649" data-title="1985" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/84649"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/84649" data-title="1985" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          1985
        </div>
        <s72-availability-label data-slug="/film/84649"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 25Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/84649" data-title="1985" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/20-days-in-mariupol/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/180248"></s72-playback-progress>
        <s72-availability-status data-slug="/film/180248"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/180248/4ea958ef8d255e15786245e4b265789c.jpg" alt="20 Days In Mariupol" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/180248" data-title="20 Days In Mariupol" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/180248"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/180248" data-title="20 Days In Mariupol" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          20 Days In Mariupol
        </div>
        <s72-availability-label data-slug="/film/180248"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 35Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/180248" data-title="20 Days In Mariupol" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/20-feet-from-stardom/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/84444"></s72-playback-progress>
        <s72-availability-status data-slug="/film/84444"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/84444/628a24afd030478c42aadbc3d63a92a1.jpg" alt="20 Feet From Stardom" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/84444" data-title="20 Feet From Stardom" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/84444"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/84444" data-title="20 Feet From Stardom" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          20 Feet From Stardom
        </div>
        <s72-availability-label data-slug="/film/84444"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 31Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/84444" data-title="20 Feet From Stardom" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/20-000-species-of-bees/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/173681"></s72-playback-progress>
        <s72-availability-status data-slug="/film/173681"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/173681/a2add958daf69fa463cd6f4fea1a1ae7.jpg" alt="20,000 Species of Bees" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/173681" data-title="20,000 Species of Bees" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/173681"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/173681" data-title="20,000 Species of Bees" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          20,000 Species of Bees
        </div>
        <s72-availability-label data-slug="/film/173681"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 5Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/173681" data-title="20,000 Species of Bees" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/2021-oscar-nominated-short-films/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/94555"></s72-playback-progress>
        <s72-availability-status data-slug="/film/94555"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/94555/b990c7bfb0032d72db11cb8598ab8076.jpg" alt="2021 Oscar Nominated Short Films" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/94555" data-title="2021 Oscar Nominated Short Films" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/94555"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/94555" data-title="2021 Oscar Nominated Short Films" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          2021 Oscar Nominated Short Films
        </div>
        <s72-availability-label data-slug="/film/94555"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 10Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/94555" data-title="2021 Oscar Nominated Short Films" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/21-grams/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/84651"></s72-playback-progress>
        <s72-availability-status data-slug="/film/84651"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/84651/39b82e0d1cf7a70c3ed501ace4e55594.jpg" alt="21 Grams" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/84651" data-title="21 Grams" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/84651"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/84651" data-title="21 Grams" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          21 Grams
        </div>
        <s72-availability-label data-slug="/film/84651"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 4Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/84651" data-title="21 Grams" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/3-faces/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/84397"></s72-playback-progress>
        <s72-availability-status data-slug="/film/84397"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/84397/ad1e7a920137f4e6a0cd90a9f147a9f9.jpg" alt="3 Faces" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/84397" data-title="3 Faces" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/84397"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/84397" data-title="3 Faces" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          3 Faces
        </div>
        <s72-availability-label data-slug="/film/84397"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 40Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/84397" data-title="3 Faces" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/3-10-to-yuma/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/84652"></s72-playback-progress>
        <s72-availability-status data-slug="/film/84652"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/84652/e0711177c2ce20bcfed5790572c65fe5.jpg" alt="3:10 To Yuma" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/84652" data-title="3:10 To Yuma" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/84652"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/84652" data-title="3:10 To Yuma" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          3:10 To Yuma
        </div>
        <s72-availability-label data-slug="/film/84652"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 2Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/84652" data-title="3:10 To Yuma" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/35-shots-of-rum/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80755"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80755"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80755/5b3bab82d62f4f19630fd6464f847954.jpg" alt="35 Shots Of Rum" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80755" data-title="35 Shots Of Rum" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80755"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80755" data-title="35 Shots Of Rum" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          35 Shots Of Rum
        </div>
        <s72-availability-label data-slug="/film/80755"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 40Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80755" data-title="35 Shots Of Rum" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/360/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80449"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80449"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80449/6b356a2131eb3808d51fa8dcd7eb847c.jpg" alt="360" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80449" data-title="360" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80449"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80449" data-title="360" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          360
        </div>
        <s72-availability-label data-slug="/film/80449"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 53Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80449" data-title="360" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/4-months-3-weeks-and-2-days/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80427"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80427"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80427/273cc4a902871ab539e4887b7cfacaf3.jpg" alt="4 Months, 3 Weeks &amp; 2 Days" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80427" data-title="4 Months, 3 Weeks &amp; 2 Days" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80427"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80427" data-title="4 Months, 3 Weeks &amp; 2 Days" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          4 Months, 3 Weeks & 2 Days
        </div>
        <s72-availability-label data-slug="/film/80427"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 53Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80427" data-title="4 Months, 3 Weeks &amp; 2 Days" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/45-years/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80367"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80367"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80367/bbf651e700c8fd51a3442073c20e0b09.jpg" alt="45 Years" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80367" data-title="45 Years" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80367"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80367" data-title="45 Years" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          45 Years
        </div>
        <s72-availability-label data-slug="/film/80367"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 35Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80367" data-title="45 Years" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/71-fragments-of-a-chronology-of-chance/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80597"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80597"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80597/327c3e524d7f9d8d50d7666278b9f6e5.jpg" alt="71 Fragments Of A Chronology Of Chance" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80597" data-title="71 Fragments Of A Chronology Of Chance" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80597"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80597" data-title="71 Fragments Of A Chronology Of Chance" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          71 Fragments Of A Chronology Of Chance
        </div>
        <s72-availability-label data-slug="/film/80597"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 40Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80597" data-title="71 Fragments Of A Chronology Of Chance" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/76-days/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/87196"></s72-playback-progress>
        <s72-availability-status data-slug="/film/87196"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/87196/d2d6f850d28920b64ff381c0013e2269.jpg" alt="76 Days" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/87196" data-title="76 Days" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/87196"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/87196" data-title="76 Days" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          76 Days
        </div>
        <s72-availability-label data-slug="/film/87196"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">1h 33Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/87196" data-title="76 Days" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
        </div>
      </div>

    </a>
  </div>



          </div>
        
          <div class="page-collection-item page-collection-list-item page-collection-list-item-landscape page-collection-item-landscape page-collection-list-item-4 page-collection-item-4">
            

  

  
  
  
  

  
    
  

  

  
  

  <div class="meta-item meta-item-landscape">
    <a href="/film/81-2/" target="" class="meta-item-link">
      <div class="poster poster-landscape">
        <s72-playback-progress slug="/film/80228"></s72-playback-progress>
        <s72-availability-status data-slug="/film/80228"></s72-availability-status>

        <img src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAQAAACRI2S5AAAAEElEQVR42mNkIAAYRxWAAQAG9gAKqv6+AwAAAABJRU5ErkJggg==" image-src="https://d2gynsnnx1ixn5.cloudfront.net/29glj/images/1920x1080/film/80228/bf18a5bca905e343d3bdc3d390c86723.jpg" alt="8½" class="curzon-image poster-image poster-image-landscape" type="landscape" border="0" />

        
          <div class="meta-item-body hover">

            <s72-play-button data-slug="/film/80228" data-title="8½" class="meta-item-play-btn meta-item-play-btn-landscape"></s72-play-button>

            <s72-classification-label data-slug="/film/80228"></s72-classification-label>

            <s72-pricing-buttons data-slug="/film/80228" data-title="8½" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
          </div>
        
      </div>

      <div class="meta-item-caption">
        
        <div class="meta-item-title ">
          8½
        </div>
        <s72-availability-label data-slug="/film/80228"></s72-availability-label>
        
        
          
  <ul class="meta-item-tagline">

    

    

    

    

    

      
        <li class="meta-item-tagline-item">2h 18Minutes</li>
      
    

    

    

  </ul>

        

        <div class="meta-item-caption-pricing-buttons">
          <s72-pricing-buttons data-slug="/film/80228" data-title="8½" class="meta-item-pricing-btn meta-item-pricing-btn-horizontal"></s72-pricing-buttons>
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

  <script defer src="https://static.cloudflareinsights.com/beacon.min.js/v84a3a4012de94ce1a686ba8c167c359c1696973893317" integrity="sha512-euoFGowhlaLqXsPWQ48qSkBSCFs3DPRyiwVu3FjR96cMPx+Fr+gpWRhIafcHwqwCqWS42RZhIudOvEI+Ckf6MA==" data-cf-beacon='{"rayId":"85eb2bcb994b4149","version":"2024.2.4","token":"c3a0d1db5bba4fdbac7b06656747c84f"}' crossorigin="anonymous"></script>
</body>
</html>"""

soup = BeautifulSoup(html_doc, 'html.parser')


def string_films():
  string = soup.get_text("\n", strip=True)
  print("Films HTML text processed")
  return string


films_list = []

def create_film_list():
  string_line = string_films.split("\n")
  films_list.extend(string_line)
  print("Film list created")
  
create_film_list()
films_list = films_list[10:-21]

print(films_list)
"""
def trim_list():
  # Trim extra website info from the list of films
  films_list = films_list[10:-21]
  # print(films_list)
"""

# Create a dictionary containing only film names and lengths
films_dict = {}

def create_film_dict():
  for i in range(0, len(films_list) - 1, 2):
    film_title = films_list[i]
    duration = films_list[i + 1]
    films_dict[film_title] = duration

# print(films_dict)

def print_summary():
  # Print header
  print(f"{'\nFilm title':<40} {'Length'}")
  print('-' * 50)

  # Print films and durations
  for film_title, duration in films_dict.items():
      print(f"{film_title:<40} {duration}")

  # Optional: Print a line to separate the output
  print('-' * 50)


string_films = string_films()
create_film_list()
# trim_list()
# create_film_dict()
# print_summary()
