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

	import topImage from './assets/MB_Background Frame_1.png' 

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

	<title>McKernan-Belgravia | School of Cities</title>

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
				title="McKernan-Belgravia Station"
				topic="Case Study"
				location="Edmonton, AB"
				subtitle="How can we build infill in a diverse community with strategic infrastructure investments to support high-capacity transit ridership?"
				image={topImage}
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
				header={"McKERNAN-BELGRAVIA STATION"}
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
				McKernan-Belgravia Station illustrates how even with a forward-thinking plan, growth near high-capacity transit can underperform when land use, density, and infrastructure are not strategically aligned. 
			</p>
			<p>
				Despite good transit access and a population inclined toward active, urban lifestyles, intensification has largely occurred through dispersed, low-intensity infill that has generated ongoing concerns about compatibility with the surrounding neighbourhood. 
			</p>
			<p>
				This case demonstrates that density alone does not guarantee ridership or community benefit: transit-oriented outcomes depend on strategic infill development that is supported by active transportation, reliable transit, and essential infrastructure. 
			</p>

			<h2 id="Menu_3">
				Neighbourhood overview 
			</h2>
			<p id="Menu_4">
				<a href="https://measuringmainstreets.ca/transit-map/" target="_blank">McKernan-Belgravia Station</a> is located on the Capital Line, Edmonton’s oldest LRT line and its busiest corridor.1 The line plays a central role in the city’s transit network, connecting major destinations including the University of Alberta and downtown, and is supported by a high-frequency transit network in the core of the city.2 
			</p>
			<p id="Menu_5">
				Edmonton Transit Service (ETS) has seen strong post-pandemic recovery, with 61.6 million riders in 2024 – a 15.2% increase from the previous year.3 Ridership reached 52.3 rides per capita,4 and 75% of riders report satisfaction with ETS.5 
			</p>
			<p>
				Within this transit-rich context, McKernan-Belgravia is a compact and diverse central neighbourhood shaped by its proximity to two University of Alberta campuses. As a mature residential neighbourhood, the area requires a strategic, sensitive approach to density – one that layers varied housing forms and essential community amenities within walking distance of the station while preserving the established residential core.    
			</p>
			<p>
				The neighbourhood’s residents are highly educated and relatively affluent. More than 60% hold a university degree, contributing to an average household income of approximately $105,000. The population is markedly youthful, with 44% of residents between the ages of 15-34, reflecting the area’s strong connection to the nearby university.  
			</p>
			<p>
				Household composition is an almost even split between family and non-family households.  While single-detached homes account for 41% of all dwellings and visually define much of the streetscape, apartment dwellings and duplexes form the majority of the housing stock at 56%. Over half of all dwellings are rented, and 70% of households are made up of one or two people. Although driving remains the largest commuter mode at 24%, well below the national average of 80.9%.,6 this community demonstrates high transit potential: the rate of walking to work is nearly six times the city average, reflecting a preference for active, urban lifestyles.  
			</p>
			<p>
				Despite these strengths, gaps in local services remain. CUI’s Complete Communities tool shows that the station area lacks key community-serving amenities, including community centres, libraries, and convenience stores. Access to supermarkets, pharmacies, and restaurants also lag behind projected demand, increasing pressure on the public realm to keep pace with density that has recently appeared.  
			</p>
			<p>
				Realizing the potential of the station area will require strategic infill and carefully planned supportive infrastructure to boost ridership and foster a destination-focused, complete community. 
			</p>
	</div>

	<!-- <Footnotes footnotes={footnotes} /> -->

	<Footer />

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
