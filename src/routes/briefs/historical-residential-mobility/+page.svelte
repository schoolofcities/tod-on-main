<script>

	import '../../../assets/global-styles.css';

	import Logo from '$lib/LogoBody.svelte';
	import TitleFullPage from '$lib/TitleFullPage.svelte';
	import TitleHalfSplit from '$lib/TitleHalfSplit.svelte';
	import TitleStandard from '$lib/TitleStandard.svelte';
	import AuthorDate from '$lib/AuthorDate.svelte';
	import ImageSingle from '$lib/ImageSingle.svelte';
	import GraphicSingle from '$lib/GraphicSingle.svelte';
	import GraphicsMultiples from '$lib/GraphicMultiples.svelte';
	import Footer from '$lib/Footer.svelte';
	import ScrollyImages from "$lib/ScrollyImages.svelte";


	import imageBus from "./assets/ttc-bus-1080.jpg";
	
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

	<title>Historical residential mobility | School of Cities</title>

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

	<!-- Full page title example -->

	<!-- <TitleFullPage
		title="Fun Captivating Project Title"
		subtitle="Maybe a slightly longer more detailed wordier project subtitle"
		image="https://jamaps.github.io/photos/picimgs/halifax2_2024.jpg"
		imageOpacity=0.9
		imageAltText="A photo"
		titleFontColour="var(--brandWhite)"
		subtitleFontColour="var(--brandWhite)"
		logoType="White"
	/> -->


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

	<div class="text" style="margin-top: 150px; margin-bottom: 20px; border-bottom: solid 1px var(--brandLightBlue);">
		<Logo/>
	</div>
	

	
	<TitleStandard
		title="Who are transit oriented development for?"
		subtitle="An historical analysis of rail transit station areas across Canada 1990-2016"
	/>

	<div class="text">

		<AuthorDate
			authors="<a href='' target='_blank'>Author Name</a> <a href='' target='_blank'>Author Name</a> & <a href='' target='_blank'>Author Name</a>"
			date="November 2025"
		/>

	</div>

	<ImageSingle
		imageURL={imageBus}
		caption=""
		source='Photo by <a href="https://unsplash.com/@json_pix?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jason Ng</a> on <a href="https://unsplash.com/photos/a-red-and-white-bus-parked-on-the-side-of-a-street-bm5UpO1_y2w?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>.'
		altText=""
		maxWidth="680px"
		link="No"
	/>

	<div class="text">
		<p>
			Access to reliable transit is a necessity for many low-income residents. It connects people to jobs, school, healthcare, grocery stores, and other essential services without the high costs of auto ownership. 
		</p>
		<p>	
			If low-income residents are displaced, especially if they are forced to move to areas with low transit accessibility, it creates barriers to access essential services and lead to social exclusion. As transit is built, keeping low-income households near these developments as well building new affordable units, helps create complete communities, reduces segregation, and ensures that the benefits of public investment in transit are shared broadly. If we fail to do this, we risk turning transit corridors into exclusive zones that serve only higher-income households, undermining goals of transportation equity and sustainability.
		</p>
		<p>
			On this page, we look at historical data in Canada (1990-2016) and ask two questions: 
			<br>
			1. Have low-income residents disproportionately moved away from areas when new transit stations are built? If so, this could signal displacement pressures linked to rising housing costs or redevelopment.
			<br>
			2. Who has moved into new transit station areas? Are they becoming more exclusive, with fewer low-income households over time? Understanding these patterns helps us see whether transit investments are reinforcing or reducing inequality.
		</p>
		<p>
			To track residential mobility, we use the Longitudinal Administrative Databank (LAD)(https://www23.statcan.gc.ca/imdb/p2SV.pl?Function=getSurvey&SDDS=4107). This dataset is a 20% sample of Canadian tax filers assembled annually since the 1980s. It includes demographic details, low-income status, and location information (census tract and six-digit postal code) for each tax filer's home address as of December 31 for each year. By looking at whether someone's postal code has changed, and if so where, we can track whether they have moved to- or from- specific station areas.
		</p>
		<p>
			Using this data, our analysis looks specifically at two key metrics:
			<br>
			1) <strong>Out-mobility:</strong> Among low-income residents living within 800 meters of a new transit station, what percentage move away within a 10-year window (five years before and five years after the station opens)? We compare this to the overall moving rate of low-income residents across the metropolitan area (CMA) to see if transit areas experience higher turnover.
			<br>
			2) <strong>In-mobility:</strong> Of those who move into the new transit station area during the same period, what percentage are low-income? We also compare this to CMA mobility rates to understand whether these areas are becoming more exclusive or inclusive.
		</p>
		<p>
			In sum, aggregating cross 
		</p>
	</div>

	<!-- GRAPHIC - out 66 68 -->

	<div class="text">
		<p>
			There is a slight difference in , but overall it , h. 
		</p>
	

	<!-- GRAPHIC - in 30 37 -->

	<p>
		The range is quite a bit larger when looking at who is moving into transit station areas. Overall, only 30% of in-movers are low-income compared to an average 37% low-income movers across CMAs in comparable time periods. This shows that transit station areas, particularly the new developments that accompany them, are more exclusive for higher-income households.
	</p>

	<p>
		How do these differences vary by city? Let's take a look
	</p>

	<!-- GRAPHIC - out by city , dumbbell -->

	<p>
		Description
	</p>

	<!-- GRAPHIC - in by city , dumbbell -->

	<p>
		Description
	</p>

	<p>
		Let's take a look at a few of the top- and bottom- performing stations ..
	</p>

	</div>

	<!-- <Footer /> -->

</main>
