<script>

	import '../../../assets/global-styles.css';

	import Logo from '$lib/LogoBody.svelte';
	import TitleFullPage from '$lib/TitleFullPageCaseStudy.svelte';
	import TitleHalfSplit from '$lib/TitleHalfSplit.svelte';
	import TitleStandard from '$lib/TitleStandard.svelte';
	import TitleVideo from '$lib/TitleVideo.svelte';
	import AuthorDate from '$lib/AuthorDate.svelte';
	import ImageSingle from '$lib/ImageSingle.svelte';
	import GraphicSingle from '$lib/GraphicSingle.svelte';
	import GraphicsMultiples from '$lib/GraphicMultiples.svelte';
	import Footer from '$lib/Footer.svelte';
	import ScrollyImages from "$lib/ScrollyImages.svelte";
	import LineBreakMiniTransitMap from '$lib/LineBreakMiniTransitMap.svelte';
	import Password from '$lib/Password.svelte';
	
	import Footnote from '$lib/Footnote.svelte';
	import Footnotes from '$lib/Footnotes.svelte';
	import { createFootnoteStore } from '$lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
	const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		'Hello I am a footnote',
		'Hello I am a second <a href="https://example.com" target="_blank">footnote</a> with a link',
		'Author (Year) Publication information etc this might be a citation or a reference to a source',
		'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla.'
	];

</script>



<svelte:head>

	<title>Embodied Carbon | School of Cities</title>

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
	<meta name="twitter:image" content="https://raw.githubusercontent.com/schoolofcities/design-components/main/static/web-card.png" /> 

	<meta name="citation_title" content="Design Components">
	<meta name="citation_author" content="Author Name 1">
	<meta name="citation_author" content="Author Name 2">
	<meta name="citation_author" content="Author Name 3"> -->
	<meta name="citation_publication_date" content="2025/09/23">
	<meta name="citation_journal_title" content="School of Cities">
	<!-- <meta name="citation_pdf_url" content="https://schoolofcities.utoronto.ca/research-paper.pdf"> -->
	<!-- <meta name="citation_abstract_html_url" content="https://schoolofcities.github.io/design-components/"> -->

</svelte:head>



<main>

	<Password correctPassword="catcatmeow"></Password>

	<TitleVideo
		title="Embodied Carbon in Different Development Patterns and Built Forms "
		subtitle=""
		titletype="RESEARCH"
		video="/tod-on-main/research/embodied-carbon/skylineVideo.mp4"
		videoSpeed={0.67}
		videoOpacity={0.8}
		titleFontColour="var(--brandWhite)"
		subtitleFontColour="var(--brandWhite)"
		logoType = 'White';
	/>


	<div class="text">

		<AuthorDate
			authors="<a href='' target='_blank'>Author Name</a> <a href='' target='_blank'>Author Name</a> & <a href='' target='_blank'>Author Name</a>"
			date="April 2026 (do we include a date?)"
		/>

	</div>

	<!-- <ImageSingle
		imageURL={imageBus}
		caption=""
		source='Photo by <a href="https://unsplash.com/@json_pix?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jason Ng</a> on <a href="https://unsplash.com/photos/a-red-and-white-bus-parked-on-the-side-of-a-street-bm5UpO1_y2w?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>.'
		altText=""
		maxWidth="680px"
		link="No"
	/> -->

	<div class="text">
		<h2>
			Why does this matter?
		</h2>
		<p>
			The concept of embodied carbon considers the greenhouse gas (GHG) impacts of development throughout its life cycle, including the emissions generated through upstream processes such as raw material extraction, manufacturing, transportation to site, and onsite energy use during construction.1 
		</p>
		<p>	
			This research evaluates the embodied GHG emissions from proposed buildings in five case study scenarios of optimized, transit-oriented development (“optimized”), and compares these emissions to a scenario that reflects current development patterns (the “current trajectory”).  
		</p>
		<p>	
			Because embodied GHG emissions occur before buildings are operational, they have immediate climate impacts. The following examples demonstrate how planning decisions shape the carbon impacts of urban growth. They also highlight opportunities to increase density while reducing emissions to help address both the climate and housing crises.   
		</p>
		<GraphicSingle
			svg720={"../research/embodied-carbon/embodied-carbon-summary-720.svg"}
			svg360={"../research/embodied-carbon/embodied-carbon-summary-720.svg"}
		/>
		<h2>
			Methodology
		</h2>
		<p>
			This study draws on a <a href="https://zenodo.org/records/7850125" target="_blank">University of Toronto database</a> that tracks the materials used in residential buildings and their associated embodied GHG emissions.2 We used it to simulate the embodied GHG emissions of new buildings under both the current trajectory and optimized scenarios, capturing variation across individual buildings and development patterns
		</p>
	</div>

	<!-- IMAGE SCHEMATIC Transport Social Exclusion -->

	

	<!-- <Footer /> -->

</main>
