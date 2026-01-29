<script>

	import '../../../assets/global-styles.css';

	import { onMount, onDestroy } from "svelte";

	import Logo from '$lib/LogoTop.svelte';
	import TitleFullPage from '$lib/TitleFullPageCaseStudy.svelte';
	import TitleHalfSplit from '$lib/TitleHalfSplit.svelte';
	import TitleStandard from '$lib/TitleStandard.svelte';
	import AuthorDate from '$lib/AuthorDate.svelte';
	import ImageSingle from '$lib/ImageSingle.svelte';
	import ImageCompare from '$lib/ImageCompare.svelte';
	import GraphicSingle from '$lib/GraphicSingle.svelte';
	import GraphicsMultiples from '$lib/GraphicMultiples.svelte';
	import Footer from '$lib/Footer.svelte';
	import FadingImages from "$lib/FadingImages.svelte";
    import ScrollAnimate from '$lib/ScrollAnimate.svelte';
	import Password from '$lib/Password.svelte';

	import topImage from './assets/AB_Background Frame_1.png' 

	import { createFootnoteStore } from '$lib/footnoteUtils';
    import { resolveRoute } from '$app/paths';
    import HamburgerMenu from '$lib/HamburgerMenu.svelte';

	export let data;

	import Footnote from '$lib/Footnote.svelte';
	import Footnotes from '$lib/Footnotes.svelte';
	const footnoteStore = createFootnoteStore();
	const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		'<a href="https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710015901" target="_blank">https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710015901</a>',
		'<a href="https://climateinstitute.ca/wp-content/uploads/2024/09/Fact-sheet_-Floods_CanadianClimateInstitute.pdf " target="_blank">https://climateinstitute.ca/wp-content/uploads/2024/09/Fact-sheet_-Floods_CanadianClimateInstitute.pdf</a>',
		'Link back to Prentiss',
		'Young Families and High-Rise: Towards Inclusive Vertical Family Housing',
		'<a href="" target="_blank"></a>'
	];

	let scrollY = 0;
	let innerHeight = 1;
	let arrowColour = "white";
	let scrollyContent = [];
	let textSection;

	// replace url with applicable content csv

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

	<title>Arbutus | School of Cities</title>

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

	<!-- <meta name="citation_title" content="Design Components"> -->
	<!-- <meta name="citation_author" content="Author Name 1"> -->
	<!-- <meta name="citation_author" content="Author Name 2"> -->
	<!-- <meta name="citation_author" content="Author Name 3"> -->
	<!-- <meta name="citation_publication_date" content="2025/09/23"> -->
	<!-- <meta name="citation_journal_title" content="School of Cities"> -->
	<!-- <meta name="citation_pdf_url" content="https://schoolofcities.utoronto.ca/research-paper.pdf"> -->
	<!-- <meta name="citation_abstract_html_url" content="https://schoolofcities.github.io/design-components/"> -->

</svelte:head>



<!-- <svelte:window on:scroll={handleScroll} /> -->

<main>
	<Password correctPassword=""></Password>
	<!-- Full page title example -->
	<div class="wrapper">
		<!-- Top stays visually on top -->
		<div class="top" style="opacity: {topOpacity}; pointer-events: {topPointer};">
			<TitleFullPage
				title="Arbutus Station"
				topic="Case Study"
				location="Vancouver, ON"
				subtitle="How can we preserve the best features of established neighbourhoods while increasing density around transit?"
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
			/>
		</div>
		<ScrollAnimate 
			colour={arrowColour}></ScrollAnimate>

		<HamburgerMenu
		iconColour={arrowColour}
		contents={data.menuItems}/>

		<!-- Bottom is underneath, scrolls normally -->
		<div class="bottom" id="before-text">
			<FadingImages
				sections={data.animations[0].items}
				header={"ARBUTUS STATION"}
				imageAlign={"center"}
				imageWidth={"100%"}
				imageHeight={"100dvh"}
				textSectionMaxWidth={"400px"}
				textSectionAlign={"left"}
				fadeDuration={1200}
				mobileTextAlign={"top"}
				backgroundColour={"#F9F9F9"}
				bind:arrowColour
			/>
		</div>

	</div>


	<div class="text">
		

			<h1 id="Menu_2">Why this matters </h1>
			<p>
				When it opens in 2027, Arbutus Station at the end of the Broadway Line will be a prominent example of ambitious transit-oriented development in a well-established neighborhood. The station is intended to support seamless multimodal travel and enhance connections to the Arbutus Greenway. This area is in many ways already a complete community, and the challenge will be ensuring the area’s affordable housing stock and many amenities keep pace with densification, so it can continue to be a home for people of all income levels.  
			</p>
			<p>	
				A core strategy must tackle valid concerns around social disruption: the threat of displacement, perceived incompatibility of uses, and risks of delayed housing and amenity delivery. 
			</p>
			<h2>
				Neighbourhood overview 
			</h2>
			<p>
				Located in Vancouver’s Kitsilano neighbourhood, Arbutus Station is an established area with more than 30,000 residents. The community is diverse: one-third are immigrants and another quarter come from outside the province. This diversity contributes to a wide range of housing needs and service demands. 
			</p>
			<p>
				This area is largely built out, with over 80% of its structures built more than 25 years ago.  
			</p>
			<p>
				Low-rise apartment units make up 775% of the households within an 800-metre radius of the station, forming the backbone of the neighbourhood’s rental stock. These older rental apartments provide naturally occurring affordable housing (NOAH), but are increasingly vulnerable to redevelopment pressures as the area densifies.4 
			</p>
			<p>
				This vulnerability is reinforced by the area’s tenure profile: 57.1% of households rent, well above the national average of 46.8%. Most residents in these units are young to middle-aged professionals living alone. Houses, while very expensive due to the area’s prime location, make up just 8% of households.  
			</p>
			<p>
				Arbutus has a vibrant main street with a wide variety of retail and services, supporting a strong local economy and steady foot traffic. 
			</p>
			<p>
				However, there are gaps in community-serving amenities such as community centres, convenience stores, and particularly libraries. Residents are also concerned that essential public services, including parks and schools, may not keep pace to serve the rapid population growth. 
			</p>
			<p>
				Supporting equitable growth here involves balancing redevelopment with the needs of current residents and the broader community. 
			</p>

	</div>

	<!-- <Footer /> -->

	<!-- <Footnotes footnotes={footnotes} /> -->

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
		z-index: 25;
		pointer-events: none; /* allows clicks to pass through if needed */
		transition: opacity 0.1s linear;
	}

	.bottom {
		position: relative;
		z-index: 1;
		min-height: 100vh; /* ensures it fills viewport behind top */
	}

	
</style>
