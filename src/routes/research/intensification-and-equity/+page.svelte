<script>

	import '../../../assets/global-styles.css';

	import Logo from '$lib/LogoBody.svelte';
	import TitlePage from '$lib/TitlePage.svelte';
	import AuthorDate from '$lib/AuthorDate.svelte';
	import ImageSingle from '$lib/ImageSingle.svelte';
	import GraphicSingle from '$lib/GraphicSingle.svelte';
	import GraphicsMultiples from '$lib/GraphicMultiples.svelte';
	import Footer from '$lib/Footer.svelte';
	import ScrollyImages from "$lib/ScrollyImages.svelte";
	import LineBreakMiniTransitMap from '$lib/LineBreakMiniTransitMap.svelte';
	import Password from '$lib/Password.svelte';
	
	import LogoBody from '$lib/LogoBody.svelte';
	import Recommendation from '$lib/Recommendation.svelte';
	import BoilerPlate from '$lib/BoilerPlate.svelte';
	import Footnote from '$lib/Footnote.svelte';
	import Footnotes from '$lib/Footnotes.svelte';
	import { createFootnoteStore } from '$lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
	const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		'Elizabeth C. Delmelle et al., “Investigating Transit-Induced Displacement Using Eviction Data,” Housing Policy Debate 31, no. 2 (2021): 326–41, <a href="https://doi.org/10.1080/10511482.2020.1815071" target="_blank">DOI</a>. ',
		'Hello I am a second <a href="https://example.com" target="_blank">footnote</a> with a link'
	];

	const credits = [
		{ role:"Research", names:"Prentiss Dantzler, Khalil Martin, and Abigail Meza"},
		{ role:"Additional writing", names:"Anika Reisha Taboy, Kathryn Exon Smith"},
		{ role:"Data visualization", names:"Polina Gorn, Jeff Allen"},
		{ role:"Web development", names:"Jeff Allen, Mieko Yao"}
	]

</script>



<svelte:head>

	<title>TOD - Intensification & Equity | School of Cities</title>

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

	<Password correctPassword="meowmeowcat"></Password>

	<TitlePage
		title="Building intensification and neighbourhood change in transit-oriented development zones "
		type="RESEARCH"
		bgType="Video"
		url="/tod-canada/web-assets/research/embodied-carbon/skylineVideo.mp4"
		videoSpeed={0.67}
		videoOpacity={0.8}
		titleFontColour="var(--brandWhite)"
		subtitleFontColour="var(--brandWhite)"
		logoType = 'White';
	/>


	<div class="text" style="margin-top: 80px">

		<AuthorDate
			credits={credits} date="March 2026"
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

		<h1>
			The big picture
		</h1>
		
		<p>
			The team at the <a href="https://www.housingjusticelab.org" target="_blank">Housing Justice Lab</a> has been tracking how new and planned rapid transit investments are reshaping neighbourhoods in five Canadian station areas. We are asking a simple but enduring question: when cities build transit, what are the effects on the ground – and for whom? Our research takes a housing justice lens, focusing on whether transit-oriented development areas promote affordability through increased building unit construction. 
		</p>

		<BoilerPlate pageType="Research"/>

		<h1>
			Methodology and approach
		</h1>

		<p>
			To understand neighbourhood change, we focused on three big pieces:
		</p>

		<ul>
			<li><span class="highlight" style="background-color: #0D534D; color: white; opacity: 0.8;">Building intensification:</span> where and how fast new housing is being built</li>
			
			<li><span class="highlight" style="background-color: #DC4633; color: white; opacity: 0.8;">Investment and landlord behaviour:</span> measured through permit values and, in Cooksville, formal eviction filings<Footnote id={addFootnote(fns[0])}/></li>
			
			<li><span class="highlight" style="background-color: #6D247A; color: white; opacity: 0.8;">Demographic change:</span> shifts among non-white, visible minority groups</li>
		</ul>

		<p>
			Methodologically, each case is built around a quasi-experimental, difference-in-differences design, comparing how station areas change relative to matched controls before and after the opening (or anticipated opening) of transit. 
		</p>

		<p>
			We used a common framework across all five sites so we could meaningfully compare what is happening in very different local contexts. In each, we defined the transit-oriented development (TOD) area as the compact, walkable, mixed-use development within 800 metres of the rapid-transit station. We delineated 800-metre station catchments around the transit station in 5 neighbourhoods: Cooksville (Mississauga), Northfield (Waterloo), Arbutus (Vancouver), McKernan–Belgravia (Edmonton), and Panama (Brossard) and used those as our station-area “treatment” groups. 
		</p>

		<p>
			We then identified matched control areas outside any rapid-transit influence with similar pre-treatment characteristics (income, renter share, dwelling condition, shelter burden, visible minority share). We created annualized indicators of development for the period before, during, and (if applicable) after construction, including: 
		</p>

		<ul>
			<li>Units created per land area and per 1,000 dwellings (where permit data allow)</li>
			
			<li>Dollar value of new dwelling projects per square kilometre</li>
			
			<li>Eviction filings per renter household in Cooksville (where eviction data allow)</li>
		</ul>

		<p>
			We also tracked ethnoracial change by census population group to see how the demographic composition of these station areas shifted over time. While this does not directly track who moved in or out, it raises subsequent questions about the drivers (e.g., migration, births, or deaths). 
		</p>

		<p>
			Click here for a more detailed discussion of the methodology. 
		</p>

		<h1>
			What we found
		</h1>

		<p>
			In general, our research found a clear, cross-case lesson: transit alone doesn’t guarantee either intensification or better access to opportunities. Local land-use rules, market conditions, and tenant protections shape who benefits from these massive public investments. 
		</p>

		<h2>
			TOD impacts are real but uneven 
		</h2>

		<p>
			The five cases show that there is great diversity of TOD effects. McKernan–Belgravia (Edmonton) had a delayed but powerful wave of infill, with a sharp spike in units per 1,000 dwellings only in the late 2010s, a decade after the station opened. Arbutus (Vancouver) and Cooksville (Mississauga) are already seeing strong pre-opening investment, as developers respond to clear planning signals (Broadway Plan, Hazel McCallion Line) and visible construction progress. Northfield (Waterloo) and Panama (Brossard) sit at the other end of the spectrum: development is emerging, but at a much slower pace, and in Panama’s case barely at all. 
		</p>

		<h2>
			Demographic change is not one story 
		</h2>

		<p>
			Across the cases, visible minority populations generally increased in station areas – but the mix is not the same everywhere. Northfield experienced one of the largest proportional jumps in visible minority residents, especially Black, Arab, Latin American, and West Asian populations, reflecting both student housing and broader migration patterns. McKernan–Belgravia and Cooksville saw growth among several racialized groups (Black, Filipino, Arab in Edmonton; Japanese and other minoritized groups in Cooksville), while some long-standing groups declined. Arbutus is diversifying in a context of entrenched land values: Latin American, Southeast Asian, and West Asian populations are growing even as overall population change remains modest. Panama largely bucks the trend: the station catchment area shows neither strong intensification nor major demographic shifts, even as surrounding South Shore areas diversify.  
		</p>

		<h2>
			Equity signals are mixed
		</h2>

		<p>
			Cooksville is our clearest window into formal displacement risk. Eviction filings per renter household declined over the decade during construction in Cooksville and other areas along the Hazel McCallion Line (formerly known as the Hurontario Light Rail Transit (LRT)), while control areas experienced higher and more volatile rates. That pattern sits uneasily next to visible reinvestment and suggests more complex sorting dynamics of who is being housed and under what conditions. 
		</p>

		<p>
			In Edmonton and Waterloo, visible minority populations are growing in station areas, but in the context of tightening rental markets and rising costs. In Panama, low development can look like “protection” from speculation, but it also means a missed opportunity to add non-market and deeply affordable housing near high-order transit.  
		</p>

		<h1>
			Specific findings from case snapshots 
		</h1>

		<p>
			A deeper examination of each case allowed us to draw conclusions from the dynamics of the case study areas compared with their municipal contexts. 
		</p>

		<h2>
			Early intensification and diversification occur where housing is affordable (for now) 
		</h2>

		<p>
			Cooksville showed a dramatic spike in the value of new dwelling projects around 2023 as the Hazel McCallion line approached opening, with much lower investment in non-station control areas. At the same time, formal eviction filings per renter household trended downward. This suggests a modest improvement in housing stability within Cooksville, potentially linked to ongoing investment and gradual neighbourhood renewal tied to the LRT.
		</p>

	</div>

	<GraphicSingle
		svg720={"../web-assets/research/intensification-and-equity/cooksville-evictions-720.svg"}
		svg360={"../web-assets/research/intensification-and-equity/cooksville-evictions-360.svg"}
	/>

	<div class="text">

		<p>
			The area’s population grew from 2016 to 2021, and the area became more racially diverse. This diversification trend aligns with broader demographic shifts along emerging transit corridors in the Greater Toronto Area, where new investment and redevelopment coincide with the movement of immigrant and racialized populations into more affordable, transit-accessible areas.<Footnote id={addFootnote(fns[1])}/>
		</p>

		<p>
			Cooksville is becoming a regional growth node, and the City has positioned Cooksville as a key redevelopment area in Mississauga’s downtown intensification strategy -- but whether that growth locks in affordability is still very much an open question.  
		</p>

		<h2>
			Emerging nodes benefit from tailored planning 
		</h2>

		<p>
			Northfield is slowly shifting from employment- and institutional-heavy lands to a more mixed urban node. Compared to station areas in central Kitchener, Northfield has a moderate concentration of newly issued housing units relative to its total land area, indicating active, but still emerging, transit-oriented development. Intensification to date has been modest in absolute terms but high relative to the existing dwelling base, suggesting that the area could experience significant redevelopment momentum in the near future. 
		</p>

		<p>
			The station area has seen a sizeable jump in visible minority residents since 2021, among the largest proportional increases in visible minority residents across the corridor.  
		</p>

	</div>

	<GraphicSingle
		svg720={"../web-assets/research/intensification-and-equity/northfield-visible-minority-720.svg"}
		svg360={"../web-assets/research/intensification-and-equity/northfield-visible-minority-360.svg"}
	/>

	<div class="text">

		<p>
			Northfield is an early-stage TOD zone where policy can still meaningfully shape outcomes. Its moderate growth demonstrates the corridor’s outward diffusion of TOD impacts. It also underscores the need for tailored planning strategies to activate underutilized lands and expand housing supply in station areas that were historically employment-focused. 
		</p>

	</div>
	

	<div class="text">

		<div class="line-break"></div>

	</div>

	<Footnotes footnotes={footnotes} />

	<div class="text">
		<div class="line-break"></div>
		<LogoBody/>
		<div class="line-break"></div>
	</div>


	

	<!-- <Footer /> -->

</main>
