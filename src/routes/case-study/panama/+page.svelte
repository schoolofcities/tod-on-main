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

	import topImage from './assets/PS_Background Frame_1.png' 

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

	<title>Panama | School of Cities</title>

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
				title="Panama Station"
				topic="Case Study"
				location="Brossard, QC"
				subtitle="How can placing civic infrastructure at the heart of redevelopment transform a suburban terminal into a vibrant transit community?  "
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
				header={"PANAMA STATION"}
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
			<h2 id="Menu_3">Neighbourhood overview   </h2>
			<p>
				Located on Montreal’s south shore, Brossard is a fast-growing suburban community of nearly 100,000 residents. Panama Station has long had a bus connection to the city, but the opening of the Réseau express métropolitain (REM) rail link in 2023 was transformative. In a region choked by congestion, the REM is a $7-billion investment in mobility, and presents an opportunity to accommodate growth where it makes the most sense, near frequent, rapid transit. Now Panama station, just 15 minutes from Montreal, is at the centre of an ambitious plan to create a new downtown for Brossard, a landmark destination with abundant housing, green space, and amenities. 1 
			</p>
			<p>	
				Today, the lands immediately adjacent to Panama Station are parking lots and underused commercial sites, with an established, low-density residential community on the periphery. These are mainly single-detached homes and some low-rise apartments, with nearly 85% built before 1990. Nearly 40% of residents are renters, a much higher rate than the rest of the city, and the median household income is modest at $64,000.  
			</p>
			<p>
				A highway and a major road bisect the site, cutting the different parts of the area off from each other. On the northern edge are a cluster of office towers and an aging shopping mall, separated by more space for parking. Over 70% of commuters drive. 
			</p>
			<p>
				Brossard is a landing point for new Canadians, and the area’s 5,300 residents are diverse: nearly half are immigrants and 60% are visible minorities. Many families live in the area, as well as a significant population of seniors. While the area has some of the elements that make a complete community – schools, grocery stores, and health care – access is low, and the area will need significant investment in both physical and social infrastructure to keep pace with growth. 
			</p>
			<p>
				The City’s vision to build a vibrant new downtown on this site is exciting, and if done right, could make a dynamic complete community here. […] 
			</p>
			<h2 id="Menu_4">
				Panama’s current trajectory  
			</h2>
			<p>
				After several years of planning and community consultation, the city council approved its Nouveaux Centre-Ville plan in 2024.2 The site plan, or Projet particulier d’urbanisme (PPU), covers a large 2.5-km swath linking the 000sqft Champlain mall at one end with City Hall and the main library at the other. Panama Station is in the middle of this band, and the area slated to see the most intensive development. The plan envisages high-rises up to 35 storeys directly adjacent to the station, with stepped changes in surrounding bands, scaling down to lower-rise (3-8 storeys) on the periphery. 
			</p>
			<p> It calls for </p>
			<ul>
				<li>Density</li>
				<li>Signature green spaces</li>
				<li>Active loop</li>
			</ul>
			<p>
				Boulevard Taschereau, a major route connecting Brossard with neighbouring Longueil, runs through the station area and is at the centre of this infrastructure redevelopment. The $500 redevelopment plan envisions this corridor also developed with TOD principles, including a focus on mid-rise density and a BRT route that links Panama Station with the metro in Longueil.3 To build out this infrastructure, the two cities will partner with the Province of Quebec and regional transit service. 
			</p>
			<p>
				Though the plan’s approval was relatively recent, the City has been laying the groundwork for development for several years. Brossard is among only a handful of station areas along the REM that have put in place bylaw changes enabling TOD, including rezoning to allow multi-family housing, raising maximum building heights, and reducing parking minimums significantly.4 
			</p>
			<p>
				In late 2025, the City approved the first development in the area, a 30-storey residential development with office, co-working, and local retail spaces on the ground floor.5 Nearly a third of the site is dedicated to public space, with 17% allocated as green space.6  
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
