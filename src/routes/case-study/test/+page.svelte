<script>

	import '../../../assets/global-styles.css';

	import { onMount, onDestroy } from "svelte";

	import Logo from '$lib/LogoTop.svelte';
	import TitleFullPage from '$lib/TitleFullPageCaseStudy.svelte';
	import TitleHalfSplit from '$lib/TitleHalfSplit.svelte';
	import TitleStandard from '$lib/TitleStandard.svelte';
	import AuthorDate from '$lib/AuthorDate.svelte';
	import ImageSingle from '$lib/ImageSingle.svelte';
	import GraphicSingle from '$lib/GraphicSingle.svelte';
	import GraphicsMultiples from '$lib/GraphicMultiples.svelte';
	import Footer from '$lib/Footer.svelte';
	import topImage from './assets/CC_Background_Frame_1.png' // TODO: MAKE THIS DARK
	import FadingImages from "$lib/FadingImages.svelte";
	import Footnote from '$lib/Footnote.svelte';
	import Footnotes from '$lib/Footnotes.svelte';
	import { createFootnoteStore } from '$lib/footnoteUtils';
    import { resolveRoute } from '$app/paths';
    import HamburgerMenu from '$lib/HamburgerMenu.svelte';
	import { navigating } from '$app/stores'


	export let data;

	const footnoteStore = createFootnoteStore();
	const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		'Hello I am a footnote',
		'Hello I am a second <a href="https://example.com" target="_blank">footnote</a> with a link',
		'Author (Year) Publication information etc this might be a citation or a reference to a source',
		'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla.'
	];


	let scrollY = 0;
	let innerHeight = 1;
	let arrowColour = "white";
	let scrollyContent = [];
	let textSection;
	let arrowHidden = false;


	let checkTextShown = () => {

	}

	onMount(() => {
		textSection = document.getElementById("top-text")
		innerHeight = window.innerHeight;

		const onScroll = () => {
			scrollY = window.scrollY;
		};

		window.addEventListener('scroll', onScroll, { passive: true });
	
		return () => window.removeEventListener('scroll', onScroll);
	});

	$: topOpacity = 1 - Math.min(scrollY / innerHeight, 1);

	$: topPointer = topOpacity < 0.02 ? 'none' : 'auto';

</script>



<svelte:head>

	<title>TOD-on-main | School of Cities</title>

	<meta name="citation_title" content="Design Components">
	<meta name="citation_author" content="Author Name 1">
	<meta name="citation_author" content="Author Name 2">
	<!-- <meta name="citation_author" content="Author Name 3"> -->
	<meta name="citation_publication_date" content="2025/09/23">
	<meta name="citation_journal_title" content="School of Cities">
	<!-- <meta name="citation_pdf_url" content="https://schoolofcities.utoronto.ca/research-paper.pdf"> -->
	<meta name="citation_abstract_html_url" content="https://schoolofcities.github.io/design-components/">

</svelte:head>



<main>

	<!-- Full page title example -->
	<div class="wrapper">
		{#if $navigating}
			<div class="m-8">
				<h1 class="ext-3xl text-center text-cText">Fetching {title}...</h1>
			</div>
		{/if}


		<div class="top" style="opacity: {topOpacity}; pointer-events: {topPointer};" aria-hidden={topOpacity === 0 ? true : false}>
			<TitleFullPage
				title="Cooksville Station"
				topic="Case Study"
				location="Mississauga, ON"
				subtitle="How do you build a high-density community bound by natural and physical land restrictions?"
				image={topImage}
				imageOpacity=1
				imageAltText="A photo"
				tintColour="black"
				tintOpacity=0.5
				titleFontColour="var(--brandWhite)"
				subtitleFontColour="var(--brandWhite)"
				authorText="Author Name, Author Name, Author Name"
				dateText="~ December, 2025"
				topOpacity={topOpacity}
				hasArrow={true}
				arrowColour="white"
			/>
		</div>
		

		<HamburgerMenu
		colour={arrowColour}
		contents={data.menuItems}/>

		<!-- Bottom is underneath, scrolls normally -->
		<div class="bottom" id="before-text">
			<FadingImages
				sections={data.animations[0].items}
				header={"COOKSVILLE STATION"}
				imageAlign={"center"}
				imageWidth={"100%"}
				imageHeight={"100dvh"}
				textSectionMaxWidth={"400px"}
				textSectionAlign={"left"}
				fadeDuration={1500}
				mobileTextAlign={"top"}
				bind:arrowColour
			/>
		</div>

	</div>

	<div id="text_1" class="text">
		<div id="top-text">
			<p>
				Fusce sed sem nulla. Praesent congue sapien pellentesque sodales fermentum. Pellentesque dapibus ultrices lacus consectetur laoreet. Integer imperdiet sed sapien sed pharetra. Praesent sodales nunc ut lorem venenatis laoreet vitae et neque. Etiam condimentum tincidunt dignissim. 
			</p>

			

			<p>	
				Praesent placerat purus vitae rhoncus auctor. Aliquam faucibus porta scelerisque. In bibendum ornare sagittis. Nam accumsan turpis sit amet elementum sollicitudin. Mauris auctor nec velit id iaculis. Proin venenatis nisl a iaculis dignissim. Nunc volutpat nulla at dolor mollis eleifend. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam commodo purus in risus placerat, sed vehicula enim viverra. 
			</p>
			<h2>
				A subheading that is nice
			</h2>
			<p>
				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla. 
			</p>
			<p>
				Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla. 
			</p>
			<p>
				Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed. 
			</p>
			<h3>
				A subheading that is nice
			</h3>
			<p>
				Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla. 
			</p>
			<p>
				Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed. 
			</p>
		</div>

		<div class="details">

			<h2>
				Extra details 
			</h2>
			<p>
				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla. 
			</p>
			<p>
				Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla. 
			</p>
			<p>
				Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed. 
			</p>

		</div>


		<Footnotes footnotes={footnotes} />
		
	</div>

	<div class="wrapper">
		<!-- Bottom is underneath, scrolls normally -->
		<div class="bottom" id="before-text">
			<FadingImages
				sections={data.animations[1].items}
				header={"COOKSVILLE STATION"}
				imageAlign={"center"}
				imageWidth={"100%"}
				imageHeight={"100dvh"}
				textSectionMaxWidth={"400px"}
				textSectionAlign={"left"}
				fadeDuration={1500}
				mobileTextAlign={"top"}
				bind:arrowColour
			/>
		</div>

	</div>

	
	<div id="text_2" class="text">
		<div id="top-text">
			<p>
				Fusce sed sem nulla. Praesent congue sapien pellentesque sodales fermentum. Pellentesque dapibus ultrices lacus consectetur laoreet. Integer imperdiet sed sapien sed pharetra. Praesent sodales nunc ut lorem venenatis laoreet vitae et neque. Etiam condimentum tincidunt dignissim. 
			</p>

			

			<p>	
				Praesent placerat purus vitae rhoncus auctor. Aliquam faucibus porta scelerisque. In bibendum ornare sagittis. Nam accumsan turpis sit amet elementum sollicitudin. Mauris auctor nec velit id iaculis. Proin venenatis nisl a iaculis dignissim. Nunc volutpat nulla at dolor mollis eleifend. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam commodo purus in risus placerat, sed vehicula enim viverra. 
			</p>
			<h2>
				A subheading that is nice
			</h2>
			<p>
				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla. 
			</p>
			<p>
				Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla. 
			</p>
			<p>
				Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed. 
			</p>
			<h3>
				A subheading that is nice
			</h3>
			<p>
				Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla. 
			</p>
			<p>
				Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed. 
			</p>
		</div>

		<div class="details">

			<h2>
				Extra details 
			</h2>
			<p>
				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla. 
			</p>
			<p>
				Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla. 
			</p>
			<p>
				Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed. 
			</p>

		</div>


		<Footnotes footnotes={footnotes} />
		
	</div>

	<!-- <Footer /> -->

</main>


<style>
	.wrapper {
		position: relative;
	}

	.top {
		position: fixed;
		inset: 0;
		height: 100vh;
		width: 100%;
		z-index: 2;
		pointer-events: none; /* allows clicks to pass through if needed */
		transition: opacity 0.1s linear;
	}

	.bottom {
		position: relative;
		z-index: 1;
		min-height: 100vh; /* ensures it fills viewport behind top */
	}

	
</style>
