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
		'Ville de Brossard, “Plan particulier d’urbanisme du centre-ville,” Annexe C du règlement REG-360, July 2, 2024, <a href="https://brossard.ca/app/uploads/2025/05/ANNEXE-29-PPU-C-V-2024-07-02_FINAL.pdf" target="_blank">URL</a>',
		'Ville de Brossard, “Plan particulier d’urbanisme du centre-ville.”',
		'Ville de Brossard, “Projects and Construction Sites - Centre-Ville de Brossard,” February 8, 2025, <a href="https://brossard.ca/en/major-projects-and-construction-sites/downtown-brossard/" target="_blank">URL</a>',
		'Henri Ouellette-Vézina, “Deux mairesses unies pour une artère durable,” <i>La Presse</i>, June 9, 2025, <a href="https://www.lapresse.ca/actualites/grand-montreal/boulevard-taschereau/vers-la-fin-d-une-fracture-urbaine/2025-06-09/boulevard-taschereau/deux-mairesses-unies-pour-une-artere-durable.php" target="_blank">URL</a>',
		'Aryana Soliz et al., “Getting into the Zone: What Can Municipal Bylaws Tell Us about Transit-Oriented Development in Montreal, Quebec?,” paper presented at 102nd Transportation Research Board Annual Meeting, 2023, <a href="https://escholarship.mcgill.ca/concern/papers/0p096d06s" target="_blank">URL</a>; Ville de Brossard, “Plan particulier d’urbanisme du centre-ville,” p. 61',
		'Henri Ouellette-Vézina, “Secteur Panama: Brossard va de l’avant avec une première tour de 30 étages,” <i>La Presse</i>, November 20, 2025, <a href="https://www.lapresse.ca/actualites/grand-montreal/2025-11-20/secteur-panama/brossard-va-de-l-avant-avec-une-premiere-tour-de-30-etages.php" target="_blank">URL</a>',
		'Ville de Brossard, “First Project Approved in the Heart of Brossard’s Future Downtown Core,” June 12, 2024, <a href="https://brossard.ca/en/news/first-project-approved-in-the-heart-of-brossards-future-downtown-core/" target="_blank">URL</a>',
		'Ville de Brossard, “Brossard’s PPU Centre-Ville Project Wins Grands Prix Du Design 2025 Award,” November 14, 2025, <a href="https://brossard.ca/en/news/brossards-ppu-centre-ville-project-wins-grands-prix-du-design-2025-award/" target="_blank">URL</a>',
		'Alexandre Fleurent, <i>Recension et analyse des stratégies et des instruments municipaux favorisant l’abordabilité en habitation : Rapport de projet en organisation</i> (2024),<a href="https://espace.enap.ca/id/eprint/521/1/Fleurent%2C%20Alexandre_org_20240829.pdf" target="_blank">URL</a>',
		'Steffen Lehmann, “Sustainable Urbanism: Towards a Framework for Quality and Optimal Density?,” <i>Future Cities and Environment</i> 2, no. 8 (2016), <a href="https://doi.org/10.1186/s40984-016-0021-3" target="_blank">DOI</a>',
		'João F. Bigotte and António P. Antunes, “Social Infrastructure Planning: A Location Model and Solution Methods,” <i>Computer-Aided Civil and Infrastructure Engineering</i> 22 (2007): 570–83, <a href="https://doi.org/10.1111/j.1467-8667.2007.00511.x" target="_blank">DOI</a>',
		'Leah Brooks and Rachel Meltzer, “Retail on the Ground and on the Books: Vacancies and the (Mis)Match Between Retail Activity and Regulated Land Uses,” <i>Journal of the American Planning Association</i> 91, no. 2 (2025): 192–206, <a href="https://doi.org/10.1080/01944363.2024.2373900" target="_blank">DOI</a>',
		'Ian Carlton and William Fleissig, <i>Steps to Avoid Stalled Equitable TOD Projects: Case Studies</i> (Living Cities, 2014), <a href="http://staging.community-wealth.org/sites/clone.community-wealth.org/files/downloads/report-carlton-fleissig-cases_0.pdf" target="_blank">URL</a>',
		'Carlton and Fleissig, <i>Steps to Avoid Stalled Equitable TOD Projects</i>',
		'Fleurent, <i>Recension et analyse des stratégies et des instruments municipaux</i>',
		'Miguel Padeiro et al., “Transit-Oriented Development and Gentrification: A Systematic Review,” <i>Transport Reviews</i> 39, no. 6 (2019): 733–54, <a href="https://doi.org/10.1080/01441647.2019.1649316" target="_blank">DOI</a>',
		'Soliz et al., “Getting into the Zone.”',
		'Jeff Allen et al., “Are Low-Income Residents Disproportionately Moving Away from Transit?,” <i>Journal of Transport Geography</i> 110 (June 2023): <a href="https://doi.org/10.1016/j.jtrangeo.2023.103635" target="_blank">DOI</a>',
		'Julie Mah, “Broadening Equitable Planning: Understanding Indirect Displacement through Seniors’ Experiences in a Resurgent Downtown Detroit,” <i>Environment and Planning A: Economy and Space</i> 55, no. 4 (2023): 905–22, <a href="https://doi.org/10.1177/0308518X221135006" target="_blank">DOI</a>',
		'Helena Hollis et al., <i>Social Infrastructure: International Comparative Review</i> (Institute for Community Studies & Bennett Institute for Public Policy, 2023), <a href="https://eprints.icstudies.org.uk/id/eprint/414/1/Social_infrastructure_international_comparative_review.pdf" target="_blank">URL</a>',
		'Mah, “Broadening Equitable Planning.”'
	];

	const credits = [
		{ role:"Research and writing", names:"Sarah Chan, Kathryn Exon Smith, Anika Reisha Taboy"},
		{ role:"Architectural renderings", names:"Daniel Lam, Phat Le"},
		{ role:"Maps and data visualization", names:"Isabeaux Graham, Jeff Allen"},
		{ role:"Web development", names:"Mieko Yao, Jeff Allen"},
		{ role:"Additional contributors", names:"An Pham, Carrie Zeng"}
	]

	let scrollY = 0;
	let innerHeight = 1;
	let arrowColour = "white";
	let scrollyContent = [];
	let textSection;

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
	<Password correctPassword="meowmeowcat"></Password>
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
				arrowColour={arrowColour}
				on:colourChange={(e) => arrowColour = e.detail}
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
			Located on Montreal’s south shore, Brossard is a fast-growing suburban community of nearly 100,000 residents. Its Panama Station has long had a bus connection to Montreal, but the opening of the Réseau express métropolitain (REM) rail link in 2023 was transformative. In a region choked by congestion, the REM is a $7-billion investment in mobility, which presents an opportunity to accommodate growth where it makes the most sense: near frequent, rapid transit. Just 15 minutes from Montreal, Panama Station is at the centre of an ambitious plan advanced by the City to create a new downtown for Brossard, a landmark destination with abundant housing, green space, and amenities.<Footnote id={addFootnote(fns[0])}/>
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
			After several years of planning and community consultation, the Brossard city council approved its <i>Nouveaux Centre-Ville</i> plan in 2024.<Footnote id={addFootnote(fns[1])}/> The site plan, or Projet particulier d’urbanisme (PPU), covers a 2.5-kilometre-long stretch linking the 715,000 square foot Champlain Mall at one end with City Hall and the main library at the other. Panama Station is in the middle of this band, and is the area slated to see the most intensive development. The plan envisages high-rises up to 35 storeys directly adjacent to the station, with stepped changes in surrounding bands, scaling down to lower-rise (3-8 storeys) on the periphery. 
		</p>
	</div>

	<ImageSingle
		imageURL={"../web-assets/case-study/panama/city_vision.jpg"}
		source={"<a href='https://brossard.ca/app/uploads/2025/05/ANNEXE-29-PPU-C-V-2024-07-02_FINAL.pdf' target='_blank'>Ville de Brossard, 2025</a>."}
		caption={"The City's vision for the station area redevelopment includes wide esplanades and signature public spaces."}
		maxWidth="1080px"
		link='No'
	/>

	<div class="text">
		<p>
			Among the core features of the plan are wide esplanades and public spaces that feature fountains and public art; pedestrian walkways connecting larger roads and making the large parcels more walkable; and designated space for sports and cultural amenities. A large central park takes inspiration from Clichy-Batignolles-Martin Luther King Park in Paris, and green space targets for individual sites scale up with greater intensity of development. A <i>boucle active</i> (active loop) will reunite the quadrants of the neighbourhood with cycling and pedestrian paths that weave over and under the highways.<Footnote id={addFootnote(fns[2])}/>
		</p>
	</div>

	<ImageSingle
		imageURL={"../web-assets/case-study/panama/bicycle_loop.png"}
		source={"<a href='https://brossard.ca/app/uploads/2025/02/Centre-ville-de-Brossard-15-1.png' target='_blank'>Ville de Brossard, 2025</a>."}
		caption={"A proposed active loop of cycling and pedestrian paths will reconnect the neighbourhood."}
		maxWidth="1080px"
		link='No'
	/>

	<div class="text">
		<p>
			Boulevard Taschereau, a major South Shore route connecting Brossard with neighbouring Longueil, runs through the station area and is at the centre of this infrastructure redevelopment. A $500-million redevelopment plan envisions this corridor also developed with TOD principles, including a focus on mid-rise density and a BRT route that links Panama Station with the metro in Longueil.<Footnote id={addFootnote(fns[3])}/>  To build out this infrastructure, the two cities will partner with the Province of Quebec and regional transit service.
		</p>
	</div>	
	
	<ImageSingle
		imageURL={"../web-assets/case-study/panama/boulevard_taschereau.jpg"}
		source={"<a href='https://brossard.ca/grands-projets-et-chantiers/revitalisation-du-boulevard-taschereau-2/' target='_blank'>Ville de Brossard, 2025</a>."}
		caption={"BoulevardTascherau's ongoing residential and commercial revitalization will add density and priority bus lanes."}
		maxWidth="1080px"
		link='No'
	/>

	<div class="text">
		<p>
			Though the downtown plan’s approval was relatively recent, the City has been laying the groundwork for development for several years. Brossard is among only a handful of station areas along the REM that have put in place bylaw changes enabling TOD, including rezoning to allow multi-family housing, raising maximum building heights, and reducing parking minimums significantly.<Footnote id={addFootnote(fns[4])}/>
		</p>
		<p>
			In late 2025, the City approved the first development in the area, a 30-storey residential development with office, co-working, and local retail spaces on the ground floor.<Footnote id={addFootnote(fns[5])}/> Nearly a third of the site is dedicated to public space, with 17% allocated as green space.<Footnote id={addFootnote(fns[6])}/>  
		</p>

		<h1 id="Menu_4">
			Optimized scenario: Making the plan a reality 
		</h1>

		<p>
			The plan for Panama Station and its surroundings is forward-thinking and visionary, embodying many best practices for TOD, and it has recently been recognized with an international award.<Footnote id={addFootnote(fns[7])}/> It also proposes lower overall density levels than many TODs in large urban areas, with the explicit intention of creating TOD on a “human scale,” and generally low- to mid-rise development outside of the areas immediately adjacent to the station. This was the outcome of extensive community consultation and a frank assessment of the capacity of the city’s infrastructure.  
		</p>
	</div>

	<ImageSingle
		imageURL={"../web-assets/case-study/panama/optimized-scenario.png"}
		source={""}
		caption={""}
		maxWidth="1080px"
		link='No'
	/>

	<!-- <ImageCompare
		imageURL1="../web-assets/case-study/panama/current-trajectory.png"
		caption1=""
		source1=""
		buttonLabel1="Current trajectory"
		imageURL2="../web-assets/case-study/panama/optimized-scenario.png"
		caption2=""
		source2=""
		buttonLabel2="Optimized scenario"
		maxWidth="900px"
		link='No'
	/> -->

	<GraphicSingle
		svg720={"../web-assets/case-study/cooksville/render-legend-720.svg"}
		svg360={"../web-assets/case-study/cooksville/render-legend-360.svg"}
	/>

	<div class="text">
		<p>
			Yet these decisions will involve trade-offs. Some larger parcels will not achieve maximum density build out, which may discourage investment and slow the pace of development, and which also lowers potential tax revenues from new residences.<Footnote id={addFootnote(fns[8])}/> Development charges to pay for parks and public spaces and the standard REM taxes levied next to stations also add to the cost of construction in a slowing market. The risk is that development stalls, never achieves its full potential, or is hampered by delays from speculation. The optimized scenario explores how to encourage early investment to create a vibrant and inclusive community.  
		</p>

		<Recommendation count=1 title="Revisit what optimal density means for this site over time"/>

		<p>
			The City’s plan recognizes the existing suburban nature and infrastructure capacity of the community and that most <i>brossardois</i> come to the area seeking low- to mid-rise density. The vision it presents respects these preferences while still offering a significant step up from the density levels of a typical North American city. The plan models a polycentric European model, similar to Paris and Barcelona, which is characterized by compact mid-rise blocks instead of dense centres that sprawl outward.<Footnote id={addFootnote(fns[9])}/>  While there is no formula for optimal density, cities must balance proximity to retail and services with the need for a sufficient population to ensure these amenities remain economically viable.<Footnote id={addFootnote(fns[10])}/> 
		</p>
	</div>

	<ImageSingle
		imageURL={"../web-assets/case-study/panama/barcelona.jpg"}
		source={"<a href='https://www.pexels.com/photo/an-aerial-view-of-barcelona-city-18602895/' target='_blank'>Archie McNicol, 2023</a>."}
		caption={"Compact mid-rise blocks, like these in Barcelona, provide sufficient density for vibrant local retail and services."}
		maxWidth="680px"
		link='No'
	/>	
	
	<div class="text">
		<p>
			In terms of retail, the plan calls for significant space dedicated to local stores along shopping esplanades. Yet these may struggle to compete with Brossard’s existing retail environment, especially with the Champlain mall within the plan area, and Canada’s largest outdoor shopping centre, the 3-million-square-foot Quartier DIX30, located just four kilometres (one REM stop) away. The amount of space dedicated to retail may need to be reduced to avoid vacant spaces.<Footnote id={addFootnote(fns[11])}/>  Zoning and floor plate sizes may need to be adjusted to accommodate anchor tenants, including retail, government, or institutional, which can encourage further development.<Footnote id={addFootnote(fns[12])}/> 
		</p>

		<Recommendation count=2 title="Invest in major infrastructure and civic spaces to spur early development"/>
		<p>
			Another approach is to repurpose this retail frontage into “civic frontage” that includes more social infrastructure from the outset, with the City leading the way in filling these storefronts. A mix of clinics, libraries, and cultural venues could exist alongside shops and cafés, a finer mix of uses that supports the area’s diverse and multicultural community. As the plan reenvisions Panama Station as the new city centre of Brossard, locating civic amenities here even above current requirements could draw foot traffic to child care centres, health care clinics, and new Canadian support services for the region, driving transit ridership. 
		</p>
		<p>
			Infrastructure can be a precondition for development and can contribute to a virtuous cycle of growth where businesses and residents locate close to transit, parks, and amenities. Yet major projects that will benefit all residents should not fall mainly to the private sector. Several successful TODs have used special district zoning to kick-start this process with tax increment financing, which can also be used for planning work and subsidizing affordable housing.<Footnote id={addFootnote(fns[13])}/>  
		</p>
	</div>

	<ImageSingle
		imageURL={"../web-assets/case-study/panama/centre_multigenerationnel.jpg"}
		source={"<a href='https://brossard.ca/grands-projets-et-chantiers/centre-multigenerationnel/' target='_blank'>Ville de Brossard, 2025.</a>."}
		caption={"Brossard's Centre Multigénérationnel opened in 2025 and is accessible by a short bus ride from Panama Station."}
		maxWidth="1080px"
		link='No'
	/>	

	<div class="text">
		<p>
			The City has laid the groundwork with investments in its three-year capital works plan, including funds in its 2026 budget for sewer expansion and an overhaul of social infrastructure such as community pools and a new multi-generational centre. The TOD plan suggests the City may also  or expropriate land for public spaces if private landowners are demanding too high a price. As a complementary approach, the City could also explore land assemblage – combining adjacent parcels into larger sites – to facilitate coordinated development and increase feasibility for higher-density projects. Other municipal levers include offering higher tax credits to early developers, and instituting a tax on specific areas (for example, vacant lots or parking to disincentivize speculation on areas near TOD and help to speed up development).<Footnote id={addFootnote(fns[14])}/>
		</p>
		<p>
			With a solid plan in place, backed by municipal zoning changes and early market interest, this is the time for other orders of government to step in with support. To avoid early projects stalling because of high development charges, the province and even federal government could step in with matching funding for major housing-enabling infrastructure. Regional, provincial, and federal programs can jump-start growth with investments in the public realm to make this an even more attractive place to invest.
		</p>

		<Recommendation count=3 title="Prioritize affordability and inclusivity"/>
		<p>
			The Panama neighbourhood is currently one of Brossard’s more affordable areas, but with a large percentage of renters and seniors on fixed incomes, it carries a high displacement risk. The residents most likely to benefit from better transit and new amenities, including lower-income households, seniors, and people who do not drive, are also the most likely to be priced out if protections aren’t built in from the start. The proposed amenities, public spaces, and easy transit access are likely to increase land values in the area – as is common with successful TOD – which could force existing community members to other less expensive areas.<Footnote id={addFootnote(fns[15])}/> 
		</p>
		<p>
			The City’s plan includes a sliding scale – recommending that affordable housing be spread throughout the development and up to 15% at the highest densities – but there is no minimum requirement at the municipal or regional level.<Footnote id={addFootnote(fns[16])}/>  This risks early development of homes that are too expensive to serve the community, and (as is often the case with TOD) too small for families, especially if they replace existing naturally affordable rental properties, often the first housing stock to be lost during redevelopment.
		</p>
		<p>
			A stronger approach is to lead with affordability. Prioritizing affordable, perhaps even social, housing construction would allow existing residents to stay in the area as development progresses, rather than being displaced to distant neighbourhoods with poor transit access. <Footnote id={addFootnote(fns[17])}/>
		</p>
		<p>
			To prevent direct displacement among seniors, some cities have worked with communities to identify buildings that house large numbers of senior residents, and employed targeted financial support to help maintain.<Footnote id={addFootnote(fns[18])}/> It will also be critical to continue serving the senior population through civic amenities, retail, and other spaces that allow them to participate in the community as it evolves. Social infrastructure, which can include civic spaces such as community centres and libraries but also commercial spaces that encourage interaction.<Footnote id={addFootnote(fns[19])}/> Locating these along pedestrian-oriented thoroughfares can encourage higher use and engagement. Ensuring a mix of accommodations and retail – particularly grocery stores, cafés, and restaurants – at all price points can promote.<Footnote id={addFootnote(fns[20])}/>  
		</p>
		<p>
			Brossard is on the cusp of major change driven by transit access and a visionary new downtown plan. Bringing this to life will require strong, early investment to kick-start positive changes, and close monitoring to ensure development remains inclusive and does not stall. By layering civic and cultural uses and a focus on affordability into an already strong plan, Panama Station can evolve from a mobility hub into a complete neighbourhood. 
		</p>
	</div>

	<ImageSingle
		imageURL={"../web-assets/case-study/panama/future_vision.jpg"}
		source={"<a href='https://brossard.ca/app/uploads/2025/02/Centre-ville-de-Brossard-16.jpg' target='_blank'>Ville de Brossard, 2025</a>."}
		caption={"A vision for the future of Panama Station."}
		maxWidth="1080px"
		link='No'
	/>

	<div class="text">
	
		<div class="line-break"></div>

		<AuthorDate credits={credits} date="March 2026"></AuthorDate>

		<div class="line-break"></div>

	</div>

	<Footnotes footnotes={footnotes} />

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
