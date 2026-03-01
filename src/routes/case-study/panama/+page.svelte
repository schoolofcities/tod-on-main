<script>

	import '../../../assets/global-styles.css';

	import { onMount, onDestroy } from "svelte";

	import Logo from '$lib/LogoTop.svelte';
	import TitlePage from '$lib/TitlePage.svelte';
	import AuthorDate from '$lib/AuthorDate.svelte';
	import ImageSingle from '$lib/ImageSingle.svelte';
	import ImageCompare from '$lib/ImageCompare.svelte';
	import GraphicSingle from '$lib/GraphicSingle.svelte';
	import GraphicMultiples from '$lib/GraphicMultiples.svelte';
	import Footer from '$lib/Footer.svelte';
	import FadingImages from "$lib/FadingImages.svelte";
    import ScrollAnimate from '$lib/ScrollAnimate.svelte';
	import Password from '$lib/Password.svelte';

	import topImage from './assets/PS_Background Frame_1.png' 

	import { createFootnoteStore } from '$lib/footnoteUtils';
    import { resolveRoute } from '$app/paths';
    import HamburgerMenu from '$lib/HamburgerMenu.svelte';

	export let data;

	import LogoBody from '$lib/LogoBody.svelte';
	import CaseStudyNote from '$lib/CaseStudyNote.svelte';
	import Recommendation from '$lib/Recommendation.svelte';
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
	<!-- <Password correctPassword="catcatmeow"></Password> -->
	<!-- Full page title example -->
	<div class="wrapper">
		<!-- Top stays visually on top -->
		<div class="top" style="opacity: {topOpacity}; pointer-events: {topPointer};">
			<TitlePage
				title="Panama Station"
				type="Case Study"
				location="Brossard, QC"
				subtitle="How can strategic development, civic infrastructure investment, and inclusive planning transform a suburban terminal into a vibrant transit-oriented community?"
				bgType="Image"
				url={topImage}
				imageOpacity=1
				imageAltText="A photo"
				tintColour="black"
				tintOpacity=0.5
				titleFontColour="var(--brandWhite)"
				subtitleFontColour="var(--brandWhite)"
				authorText="Author Name, Author Name, Author Name"
				dateText="~ December, 2025"
				secondLogo="II"
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

		<p>
			This case explores how to bring Brossard’s complete community vision to fruition while ensuring it stays affordable and inclusive. 
		</p>

		
		<CaseStudyNote/>

		<h2 id="Menu_2">Neighbourhood overview   </h2>

		<p>
			Located on Montreal’s south shore, Brossard is a fast-growing suburban community of nearly 100,000 residents. Its Panama Station has long had a bus connection to Montreal, but the opening of the Réseau express métropolitain (REM) rail link in 2023 was transformative. In a region choked by congestion, the REM is a $7-billion investment in mobility, which presents an opportunity to accommodate growth where it makes the most sense: near frequent, rapid transit. Just 15 minutes from Montreal, Panama Station is at the centre of an ambitious plan advanced by the City to create a new downtown for Brossard, a landmark destination with abundant housing, green space, and amenities.1 
		</p>

	</div>

	<GraphicSingle
		svg720={"../web-assets/case-study/panama/Panama-720map.svg"}
		svg360={"../web-assets/case-study/panama/Panama-360map.svg"}
	/>

	<div class="text">

		<p>	
			Today, the lands immediately adjacent to Panama Station are parking lots and underused commercial sites, with an established, low-density residential community on the periphery. These are mainly single-detached homes and some low-rise apartments, with nearly 85% built before 1990. Nearly 40% of residents are renters, a much higher rate than in the rest of the city, and the median household income is modest at $64,000.  
		</p>
		<p>
			Two provincial highways – Autoroute 10 and Boulevard Taschereau – bisect the site, cutting the different parts of the area off from each other. A cluster of office towers and an aging shopping mall sit on the northern edge of the station area, separated by more space for parking. Over 70% of commuters drive. 
		</p>
		<p>
			Brossard is a landing point for new Canadians, and the station area’s 5,300 residents are diverse: nearly half are immigrants and 60% are visible minorities. Many families live in the area, as well as a significant population of seniors. While the area has some of the elements that make a complete community – schools, grocery stores, and health care – access is generally low, and the area will need significant investment in both physical and social infrastructure to keep pace with growth. 
		</p>

	</div>

	<GraphicMultiples
		svgPaths={[
			"../web-assets/case-study/panama/Panama-immigrants.svg",
			"../web-assets/case-study/panama/Panama-commuters.svg",
			"../web-assets/case-study/panama/Panama-renters.svg",
			"../web-assets/case-study/panama/Panama-income.svg"
		]}
	/>

	<div class="text">

		<div class="caption-container" style="margin-top: 0px; margin-bottom: 60px;">
			<p>
				<span class="caption-source">Data sources: Statistics Canada, Environics Analytics (2024).</span>
			</p>
		</div>

		<p>
			The City’s vision to build a vibrant new downtown on this site is exciting, and if done right, could make a dynamic complete community here.  
		</p>

		<h1 id="Menu_3">
			Panama’s current trajectory  
		</h1>

		<p>
			After several years of planning and community consultation, the Brossard city council approved its Nouveaux Centre-Ville plan in 2024.2 The site plan, or Projet particulier d’urbanisme (PPU), covers a 2.5-kilometre-long stretch linking the 715,000 square foot Champlain Mall at one end with City Hall and the main library at the other. Panama Station is in the middle of this band, and is the area slated to see the most intensive development. The plan envisages high-rises up to 35 storeys directly adjacent to the station, with stepped changes in surrounding bands, scaling down to lower-rise (3-8 storeys) on the periphery. 
		</p>
		<p>
			Boulevard Taschereau, a major South Shore route connecting Brossard with neighbouring Longueil, runs through the station area and is at the centre of this infrastructure redevelopment. A $500-million redevelopment plan envisions this corridor also developed with TOD principles, including a focus on mid-rise density and a BRT route that links Panama Station with the metro in Longueil.4 To build out this infrastructure, the two cities will partner with the Province of Quebec and regional transit service. 
		</p>
		<p>
			Though the downtown plan’s approval was relatively recent, the City has been laying the groundwork for development for several years. Brossard is among only a handful of station areas along the REM that have put in place bylaw changes enabling TOD, including rezoning to allow multi-family housing, raising maximum building heights, and reducing parking minimums significantly.5 
		</p>
		<p>
			In late 2025, the City approved the first development in the area, a 30-storey residential development with office, co-working, and local retail spaces on the ground floor.6 Nearly a third of the site is dedicated to public space, with 17% allocated as green space.7  
		</p>

		<h1 id="Menu_4">
			Optimized scenario: Making the plan a reality 
		</h1>

		<p>
			The plan for Panama Station and its surroundings is forward-thinking and visionary, embodying many best practices for TOD, and it has recently been recognized with an international award.8 It also proposes lower overall density levels than many TODs in large urban areas, with the explicit intention of creating TOD on a “human scale,” and generally low- to mid-rise development outside of the areas immediately adjacent to the station. This was the outcome of extensive community consultation and a frank assessment of the capacity of the city’s infrastructure.  
		</p>
		<p>
			Yet these decisions will involve trade-offs. Some larger parcels will not achieve maximum density build out, which may discourage investment and slow the pace of development, and which also lowers potential tax revenues from new residences.9 Development charges to pay for parks and public spaces and the standard REM taxes levied next to stations also add to the cost of construction in a slowing market. The risk is that development stalls, never achieves its full potential, or is hampered by delays from speculation. The optimized scenario explores how to encourage early investment to create a vibrant and inclusive community.  
		</p>

	</div>

	<div class="text">
	
		<div class="line-break"></div>

		<!-- <AuthorDate credits={credits} date="March 2026"></AuthorDate> -->

		<div class="line-break"></div>

	</div>

	<!-- <Footnotes footnotes={footnotes} /> -->

	<div class="text">
		<div class="line-break"></div>
		<LogoBody/>
		<div class="line-break"></div>
	</div>

	<!-- <Footnotes footnotes={footnotes} /> -->
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
