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
	import featureImage from './assets/cooksville-transit-schematic.png'

	import FadingImages from "$lib/FadingImages.svelte";

	export let data;

	// const scrollyContentSmall = [
	// 	{
	// 		image: "./examples/amroth-iso-lot.png",
	// 		text: "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>"
	// 	},
	// 	{
	// 		image: "./examples/amroth-iso-bldg.png",
	// 		text: "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>"
	// 	},
	// 	{
	// 		image: "./examples/wilson-iso-lot.svg",
	// 		text:"<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>"
	// 	},
	// 	{
	// 		image: "./examples/wilson-iso-bldg.svg",
	// 		text: "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>"
	// 	},
	// ];
	
	import Footnote from '$lib/Footnote.svelte';
	import Footnotes from '$lib/Footnotes.svelte';
	import { createFootnoteStore } from '$lib/footnoteUtils';
    import BottomArrow from '$lib/BottomArrow.svelte';
    import { resolveRoute } from '$app/paths';
    import HamburgerMenu from '$lib/HamburgerMenu.svelte';

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

	// replace url with applicable content csv

	onMount(() => {
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

	<!-- <meta name="description" content="Repository of design and web components for building data stories, visualizations, maps, and other custom web projects" />
	<meta name="author" content="School of Cities">
	<meta rel="canonical" href="https://schoolofcities.github.io/design-components/">

	<meta property="og:title" content="Design Components" />
	<meta property="og:description" content="Repository of design and web components for building data stories, visualizations, maps, and other custom web projects" />
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://schoolofcities.github.io/design-components/" />
	<meta property="og:image" content="https://raw.githubusercontent.com/schoolofcities/design-components/main/static/web-card.png" />
	<meta property="og:locale" content="en_CA">

	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:title" content="Design Components" />
	<meta name="twitter:description" content="Repository of design and web components for building data stories, visualizations, maps, and other custom web projects" />
	<meta name="twitter:site" content="https://schoolofcities.github.io/design-components/" />
	<meta name="twitter:image" content="https://raw.githubusercontent.com/schoolofcities/design-components/main/static/web-card.png" />  -->

	<meta name="citation_title" content="Design Components">
	<meta name="citation_author" content="Author Name 1">
	<meta name="citation_author" content="Author Name 2">
	<!-- <meta name="citation_author" content="Author Name 3"> -->
	<meta name="citation_publication_date" content="2025/09/23">
	<meta name="citation_journal_title" content="School of Cities">
	<!-- <meta name="citation_pdf_url" content="https://schoolofcities.utoronto.ca/research-paper.pdf"> -->
	<meta name="citation_abstract_html_url" content="https://schoolofcities.github.io/design-components/">

</svelte:head>



<!-- <svelte:window on:scroll={handleScroll} /> -->

<main>

	<!-- Full page title example -->
	<div class="wrapper">
		<!-- Top stays visually on top -->
		<div class="top" style="opacity: {topOpacity}; pointer-events: {topPointer};">
			<TitleFullPage
				title="Cooksville Station"
				topic="Case Study"
				location="Mississauga, ON"
				subtitle="How do you build a high-density community bound by natural and physical land restrictions?"
				image={topImage}
				imageOpacity=1
				imageAltText="A photo"
				imageFeature={featureImage}
				tintColour="black"
				tintOpacity=0.5
				titleFontColour="var(--brandWhite)"
				subtitleFontColour="var(--brandWhite)"
				authorText="Author Name, Author Name, Author Name"
				dateText="~ December, 2025"
				topOpacity={topOpacity}
			/>
		</div>
		
		<BottomArrow 
		clickable={true}
		colour={arrowColour}/>

		<HamburgerMenu
		colour={arrowColour}/>

		<!-- Bottom is underneath, scrolls normally -->
		<div class="bottom">
			<FadingImages
				sections={data.rows}
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





	
	

	

	

	


	<!-- Here is a half split title example: -->

	<!-- <TitleHalfSplit
		title="Fun Captivating Project Title"
		subtitle="Maybe a slightly longer more detailed wordier project subtitle that explains the project"
		image="https://schoolofcities.github.io/eddit/_app/immutable/assets/wood-buffalo-title-img-2.CpYjt7SE.jpg"
		imageAltText="A photo"
		imageCaption="Wood Buffalo skyline."
		imageSource="Wikimedia Commons."
		titleFontColour="var(--brandWhite)"
		titleBorderColour="var(--brandYellow)"
		subtitleFontColour="var(--brandWhite)"
		backgroundColour="var(--brandDarkBlue)"
		logoStyle="Dark"
	/> -->

	
	<!-- Simple title example with logo and subtitle: -->

	<!-- <Logo logoType="Blue" backgroundColor="var(--brandWhite)"/>

	<ImageSingle
		imageURL="https://jamaps.github.io/photos/picimgs/taipei1_2025.jpg"
		caption="Taipei skyline."
		source="Jeff Allen."
		altText=""
		maxWidth="1080px"
	/>


	<TitleStandard
		title="Fun Captivating Project Title"
		subtitle="Maybe a slightly longer more detailed wordier project subtitle "
	/>

	<div class="text">

		<AuthorDate
			authors="<a href='' target='_blank'>Author Name</a> & <a href='' target='_blank'>Author Name</a>"
			date="July 2025"
		/>

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla. 
		</p>

		<p>
			Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci.<Footnote id={addFootnote(fns[0])}/> nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla.
		</p>

		<p>
			Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed.<Footnote id={addFootnote(fns[1])} />
		</p>

		<p>
			Nunc vel massa turpis. Vivamus id odio ut nulla dignissim molestie. 
		</p>

	</div>

	<GraphicSingle
		svg720="./examples/map-tree-redline-720.svg"
		svg360="./examples/map-tree-redline-360.svg"
	/>
	
	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla.<Footnote id={addFootnote(fns[2])} />
		</p>
		<p>
			Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla.<Footnote id={addFootnote(fns[3])} />
		</p>
		<p>
			Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed.<Footnote id={addFootnote(fns[0])} />
		</p>
		<p>
			Nunc vel massa turpis. Vivamus id odio ut nulla dignissim molestie. 
		</p>

	</div>

	<GraphicsMultiples
		svgPaths={["./examples/map-tree-360.svg", "./examples/map-heat-360.svg", "./examples/map-asthma-360.svg"]}
	/>

	

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla.<Footnote id={addFootnote(fns[2])} />
		</p>
		<p>
			Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla.<Footnote id={addFootnote(fns[3])} />
		</p>
		<p>
			Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed.<Footnote id={addFootnote(fns[0])} />
		</p>
		<p>
			Nunc vel massa turpis. Vivamus id odio ut nulla dignissim molestie. 
		</p>

	</div> -->

	<!-- <ScrollyImages
		sections={scrollyContentSmall}
		imageAlign={"center"}
		imageWidth={"540px"}
		imageHeight={"540px"} 
		textSectionMaxWidth={"540px"}
		textSectionAlign={"right"}
		fadeDuration={500}
	/> -->

	


	
	<div class="text">
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



	<div class="text">

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

	</div>

	<div class="text">

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
