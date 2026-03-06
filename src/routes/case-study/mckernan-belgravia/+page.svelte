<script>

	import '../../../assets/global-styles.css';

	import { onMount, onDestroy } from "svelte";

	import Logo from '$lib/LogoTop.svelte';
	import AuthorDate from '$lib/AuthorDate.svelte';
	import ImageSingle from '$lib/ImageSingle.svelte';
	import ImageCompare from '$lib/ImageCompare.svelte';
	import GraphicSingle from '$lib/GraphicSingle.svelte';
	import GraphicMultiples from '$lib/GraphicMultiples.svelte';
	import Footer from '$lib/Footer.svelte';
	import FadingImages from "$lib/FadingImages.svelte";
    import ScrollAnimate from '$lib/ScrollAnimate.svelte';
	import Password from '$lib/Password.svelte';

	import topImage from './assets/MB_Background Frame_1.png' 

	import { createFootnoteStore } from '$lib/footnoteUtils';
    import { resolveRoute } from '$app/paths';
    import HamburgerMenu from '$lib/HamburgerMenu.svelte';

	export let data;

	import LogoBody from '$lib/LogoBody.svelte';
	import Recommendation from '$lib/Recommendation.svelte';
	import CaseStudyNote from '$lib/CaseStudyNote.svelte';
	import Footnote from '$lib/Footnote.svelte';
	import Footnotes from '$lib/Footnotes.svelte';
    import TitlePage from '$lib/TitlePage.svelte';
    import ImageMultiples from '$lib/ImageMultiples.svelte';
	const footnoteStore = createFootnoteStore();
	const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		'City of Edmonton, “Capital Line,” accessed February 23, 2026, <a href="https://www.edmonton.ca/projects_plans/transit/capital-line" target="_blank">URL</a>',
		'City of Edmonton, <i>Edmonton Transit Service 2024/2025 Annual Service Plan</i> (2025), <a href="https://www.edmonton.ca/sites/default/files/public-files/2024-2025-Edmonton-Transit-Service-Annual-Service-Plan.pdf?cb=1742837639" target="_blank">URL</a>',
		'Statistics Canada, “Number of Canadian Commuters Increases for Fourth Straight Year in 2025,” <i>The Daily</i>, August 26, 2025, <a href="https://www150.statcan.gc.ca/n1/daily-quotidien/250826/dq250826a-eng.htm" target="_blank">URL</a>',
		'Barry Johns, <i>Effective Urban Densification: A Guide for Professionals and the Housing Industry</i>, 1st ed. (Routledge, 2024), <a href="https://doi.org/10.4324/9781003414803" target="_blank">DOI</a>',
		'Julian Bolleter et al., “Delivering Medium‑Density Infill Development Through Promoting the Benefits and Limiting Background Infill,” <i>Journal of Urban Design</i> (2020), <a href="https://doi.org/10.1080/13574809.2020.1854610" target="_blank">DOI</a>',
		'Bolleter et al., “Delivering Medium‑Density Infill Development.”',
		'“Refocusing Infill: How Can We Build More Family-Friendly, More Affordable Housing Choices at LRT Stations?,” Michael Janz (website), August 5, 2025, <a href="https://www.michaeljanz.ca/tod" target="_blank">URL</a>',
		'Bolleter et al., “Delivering Medium‑Density Infill Development.”',
		'Ehab Diab et al., “The Rise and Fall of Transit Ridership Across Canada: Understanding the Determinants,” <i>Transport Policy</i> 96 (2020): 101-112, <a href="https://doi.org/10.1016/j.tranpol.2020.07.002" target="_blank">DOI</a>',
		'Corinne Mulley et al., “Land Value Gains and Value Capture: The Potential for Financing Public Transport Infrastructure,” <i>The Routledge Handbook of Public Transport</i> (2021), 123–137.',
		'City of Edmonton, <i>Executive Summary: 2024 Rider Research Program</i>, <a href="https://www.edmonton.ca/sites/default/files/public-files/ETS-Rider-Research-Program-2024-Executive-Summary.pdf?cb=1769545549" target="_blank">URL</a>',
		'City of Edmonton, <i>Edmonton Transit Service 2024/2025 Annual Service Plan</i> (2025), <a href="https://www.edmonton.ca/sites/default/files/public-files/2024-2025-Edmonton-Transit-Service-Annual-Service-Plan.pdf?cb=1742837639" target="_blank">URL</a>',
		'Robin Lindsey et al., “Distributional Effects of Urban Transport Policies to Discourage Car Use: A Literature Review,” <i>OECD Environment Working Papers</i> No. 211 (2023), <a href="https://doi.org/10.1787/8bf57103-en" target="_blank">DOI</a>',
		'Lindsey et al., “Distributional Effects of Urban Transport Policies to Discourage Car Use.”',
		'Mohammed AlHasawi et al., “Key Success Factors of Urban Infill Development: A Conceptual Framework,” <i>European Journal of Architecture and Urban Planning</i> 3, no. 3 (2024): 9-17, <a href="https://doi.org/10.24018/ejarch.2024.3.3.40" target="_blank">DOI</a>',
		'Meg Holden, “Bringing the Neighbourhood Into Urban Infill Development in the Interest of Well-Being," <i>International Journal of Community Well-Being</i> 1 (2019): 137–155, <a href="https://doi.org/10.1007/s42413-018-0010-4" target="_blank">DOI</a>',
		'Meg Holden, “Bringing the Neighbourhood Into Urban Infill Development in the Interest of Well-Being," <i>International Journal of Community Well-Being</i> 1 (2019): 137–155, <a href="https://doi.org/10.1007/s42413-018-0010-4" target="_blank">DOI</a>'
	];

	let scrollY = 0;
	let innerHeight = 1;
	let arrowColour = "black";
	let scrollyContent = [];
	let textSection;

	const credits = [
		{ role:"Research and writing", names:"Sarah Chan, Kathryn Exon Smith, Anika Reisha Taboy"},
		{ role:"Architectural renderings", names:"Daniel Lam, Phat Le"},
		{ role:"Maps and data visualization", names:"Isabeaux Graham, Jeff Allen"},
		{ role:"Web development", names:"Mieko Yao, Jeff Allen"},
		{ role:"Additional contributors", names:"An Pham, Carrie Zeng"}
	]

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
	<Password correctPassword="meowmeowcat"></Password>
	<!-- Full page title example -->
	<div class="wrapper">
		<!-- Top stays visually on top -->
		<div class="top" style="opacity: {topOpacity}; pointer-events: {topPointer};">
			<TitlePage
				title="McKernan-Belgravia Station"
				type="Case Study"
				location="Edmonton, AB"
				subtitle="How can we build infill in a mature community with strategic infrastructure investments to support high-capacity transit ridership?"
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
				header={"McKERNAN-BELGRAVIA STATION"}
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
			This case demonstrates that permissive zoning and the presence of a transit station alone do not guarantee density – or the ridership and community benefits that density enables. Those outcomes depend on market factors, deliberate infill, and planning for the elements that make transit-oriented living work: active transportation, reliable transit, and essential infrastructure.
		</p>
		
		<CaseStudyNote/>

		<h2 id="Menu_2">
			Neighbourhood overview 
		</h2>
		<p>
			<a href="https://measuringmainstreets.ca/transit-map/" target="_blank">McKernan-Belgravia Station</a> is located on the busiest corridor of the Capital Line, Edmonton’s oldest light rail transit (LRT) route.<Footnote id={addFootnote(fns[0])}/>  The line plays a central role in the city’s transit network, connecting major destinations including the University of Alberta and downtown, and is supported by a high-frequency transit network in the city’s core.<Footnote id={addFootnote(fns[1])}/> 
		</p>
		<p>
			Within this transit-rich context, McKernan-Belgravia is a mature, central neighbourhood that requires a strategic, sensitive approach to density – one that layers varied housing forms and essential community amenities within walking distance of the station while preserving the established residential core. 
		</p>

	</div>

	<GraphicSingle
		svg720={"../web-assets/case-study/mckernan-belgravia/McKernanBelgravia-720map.svg"}
		svg360={"../web-assets/case-study/mckernan-belgravia/McKernanBelgravia-360map.svg"}
	/>

	<GraphicMultiples
		svgPaths={[
			"../web-assets/case-study/mckernan-belgravia/Mckernanbelgravia-residents.svg",
			"../web-assets/case-study/mckernan-belgravia/Mckernanbelgravia-housing.svg",
			"../web-assets/case-study/mckernan-belgravia/Mckernanbelgravia-income.svg",
			"../web-assets/case-study/mckernan-belgravia/Mckernanbelgravia-commuters.svg"
		]}
	/>

	<div class="text">

		<div class="caption-container" style="margin-top: 0px; margin-bottom: 60px;">
			<p>
				<span class="caption-source">Data sources: Statistics Canada, Environics Analytics (2024).</span>
			</p>
		</div>

		<p>
			The neighbourhood’s residents are highly educated and relatively affluent. More than 60% hold a university degree, contributing to an average household income of approximately $160,000. The population is markedly young, with 44% of residents aged 15-34, reflecting the area’s strong connection to the nearby university. 
		</p>
		<p>
			Household composition is an almost even split between family and non-family households. While single-detached homes account for 41% of all dwellings and visually define much of the streetscape, apartment dwellings and duplexes form the majority of the housing stock, at 56%. Over half of all dwellings are rented, and 70% of households are made up of one or two people. Although driving remains the largest commuter mode at about 56% – well below the national average of 8%<Footnote id={addFootnote(fns[2])}/> – this community demonstrates high transit potential: the rate of walking to work is nearly si times the city average, reflecting a preference for active, urban lifestyles. 
		</p>
		<p>
			Despite these strengths, gaps in local services remain. The station area <a href="https://measuringmainstreets.ca/tools/complete-communities" target="_blank">lacks key community-serving amenities</a>, including community centres, libraries, and convenience stores. Access to supermarkets, pharmacies, and restaurants also lags behind projected demand, increasing pressure on the public realm to keep pace with the gentle density that has recently appeared. Realizing the potential of the station area will require strategic infill and carefully planned supportive infrastructure to boost ridership and foster a destination-focused, complete community. 
		</p>

		<h1 id="Menu_3">
			McKernan-Belgravia's current trajectory
		</h1>

		<p>
			In response to rising housing demand, Edmonton introduced a city-wide <a href="https://www.edmonton.ca/city_government/urban_planning_and_design/zoning-bylaw-renewal" target="_blank">Zoning Bylaw Renewal Initiative</a> in 2024, which permits 8-plexes as-of-right and eliminates the requirement for neighbour notification or consultation if proposals fall within the guidelines. The bylaw also supports larger developments on larger corner lots and along designated main corridors. Coupled with the removal of minimum parking requirements in 2020, these policies have increased flexibility for incremental development but have also made small-scale infill easier to deliver than coordinated medium-density forms.
		</p>

		<p>
			The City’s vision calls for strategic density: medium-scale, mixed-use buildings – generally mid-rise forms with active ground floors – along major arterials like 114 Street and 76 Avenue, complemented by new amenities and multimodal routes, with more modest infill within the neighbourhood fabric. 
		</p>
	</div>

	<ImageSingle
		imageURL="../web-assets/case-study/mckernan-belgravia/redevelopment_plan.jpg"
		source={"<a href='https://webdocs.edmonton.ca/infraplan/plans_in_effect/McKernan-Belgravia_Station_ARP_Consolidation.pdf' target='_blank'>Photo by the City of Edmonton, 2024</a>."}
		caption={"The City's vision for growth in the McKernan-Belgravia Station Area, shown here in their Redevelopment Plan, envisions medium-scale density along major corridors."}
		maxWidth="680px"
		link='No'
	/>

	<div class="text">
		<p>
			In practice, however, most development activity has been small-scale infill embedded within existing residential streets. Of 38 active proposals at the time of this study, only five propose more than eight units, while three- and four-unit rowhouses dominate. This pattern reflects the ease of developing individual lots compared to assembling sufficient land to deliver medium-density forms along major roads. 
		</p>

		<p>
			In theory, building on single-family lots aligns with best practices for mature neighbourhoods: this retention-based infill can maintain neighbourhood character, support affordability, and reduce displacement.<Footnote id={addFootnote(fns[3])}/>  In Edmonton’s case, however, the cumulative pace and scale of change has left some residents feeling overwhelmed and frustrated. In part this is because the new city-wide infill bylaw reduced opportunities for consultation and rescinded previous neighbourhood plans, which were the result of robust community engagement. Some residents believe the new process lacks the legitimacy of community support, and have voiced concerns around building scale, design compatibility, reduction of tree canopy, and influence on property values. The new infill patterns are also influenced by corporate investment, with some community members feeling squeezed out by developers who purchase large numbers of individual lots with the intention of constructing multi-unit short-term rentals priced higher than existing rental stock.
		</p>

		<p>
			Edmonton remains one of Canada’s most affordable cities, and TOD is often competing with single-family homes in more suburban areas at the same price. Done well, new developments in the McKernan-Belgravia station area can show the best of urban living, with easy access to the two University of Alberta campuses nearby. But if growth continues to prioritize incremental infill with limited mid-rise development, the opportunity to create a vibrant, transit-supportive sense of place may remain unrealized. Without high-quality amenities, an improved public realm, and strong transit service, TOD in communities like this risks being perceived as denser, but not necessarily more desirable, than car-oriented communities further from the core. 
		</p>

		<h1 id="Menu_4">
			Optimized scenario: Aligning growth and infrastructure to incentivize transit use 
		</h1>

		<p>
			Our optimized scenario responds to a core challenge in McKernan-Belgravia: infill has not been sufficiently integrated or aligned with the intent of the City’s plan of concentrating growth in larger developments along major corridors. A central piece therefore is the creation of a destination-focused station area. Locating development where transit access is strongest allows density to function as a catalyst for amenities, activity, and daily destinations.
		</p>

		<p>
			Recent development has raised concerns that housing quantity is being prioritized over quality. We suggest that deliberate attention to building scale, setbacks, and massing near existing homes could improve social acceptance. Supporting measures include addressing common resident concerns such as tree canopy preservation, enhanced public amenities, and traffic and waste management improvements. 
		</p>

	</div>

	<ImageCompare
		imageURL1="../web-assets/case-study/mckernan-belgravia/current-trajectory.png"
		caption1=""
		source1=""
		buttonLabel1="Current trajectory"
		imageURL2="../web-assets/case-study/mckernan-belgravia/optimized-scenario.png"
		caption2=""
		source2=""
		buttonLabel2="Optimized scenario"
		maxWidth="900px"
		link='No'
	/>

	<GraphicSingle
		svg720={"../web-assets/case-study/cooksville/render-legend-720.svg"}
		svg360={"../web-assets/case-study/cooksville/render-legend-360.svg"}
	/>

	<div class="text">	

		<p>
			In McKernan-Belgravia, achieving transit-oriented outcomes depends on how development is delivered, not just how much housing is added. In a mature neighbourhood, infill must be paired with supportive infrastructure, amenities, and public realm improvements to create a complete community. Re-aligning development patterns, encouraging active modes and transit use, and addressing community concerns will help concentrate activity around the station, foster a sense of place, and support higher transit use.
		</p>

	</div>

	<ImageSingle
		imageURL={"../web-assets/case-study/mckernan-belgravia/lrt_station.jpg"}
		source={"<a href='https://commons.wikimedia.org/wiki/File:McKernan_Belgravia_LRT_Station_(3474530058).jpg' target='_blank'>Photo by Mack Male, 2009</a>."}
		caption={"McKernan-Belgravia Station in 2009, the year it opened as part of Edmonton's Capital Line extension."}
		maxWidth="680px"
		link='No'
	/>		

	<div class="text">

		<Recommendation count=1 title="Guide medium-density growth along corridors through zoning and street design"/>

		<p>
			McKernan-Belgravia illustrates the risks of highly permissive uniform rezoning approaches, which allow low-rise development across all neighbourhoods under standardized regulations. The result is “background” infill – small-scale, incremental development on residential lots. While this form of infill can increase housing supply, it often delivers only marginal density gains, lacks coordinated amenities or green space, and diffuses development away from corridors intended to support higher-intensity growth.
		</p>

		<p>
			Evidence from comparable cities, including Perth, Australia, suggests this pattern can also undermine medium-density infill by making individual lot redevelopment easier than assembling land for more efficient projects. Poorly coordinated background infill has been associated with limited design responsiveness, loss of mature trees, predominantly paved sites, and minimal contributions to neighbourhood amenities – ultimately generating community pushback.<Footnote id={addFootnote(fns[4])}/> 
		</p>

		<p>
			Municipalities can mandate a minimum lot size for infill – reducing the viability of background infill and shifting the market toward medium-density projects – or incentivize lot amalgamation through density bonuses, financial incentives, or zoning mechanisms that enable higher densities for combined lots.<Footnote id={addFootnote(fns[5])}/>  One councillor has proposed temporary tax abatements for family-friendly mid-rise (six or more storeys) built within 400 metres of LRT stations as a way to encourage this kind of development, a measure supported by local infill advocates.<Footnote id={addFootnote(fns[6])}/>  Larger, assembled sites provide greater design flexibility and reduce the perceived impacts of medium-density development.<Footnote id={addFootnote(fns[7])}/> 
		</p>

	</div>
	
	<ImageSingle
		imageURL={"../web-assets/case-study/mckernan-belgravia/housing_accelerator.jpg"}
		source={"<a href='https://www.edmonton.ca/programs_services/housing/housing-accelerator-fund' target='_blank'>Photo by the City of Edmonton, 2024</a>."}
		caption={"Medium-density rowhouses on large corner lots, like those pictured here, can help to increase density around transit and support amenities and infrastructure."}
		maxWidth="680px"
		link='No'
	/>

	
	<ImageSingle
		imageURL={"../web-assets/case-study/mckernan-belgravia/grovenor.jpg"}
		source={"<a href='https://www.edmonton.ca/sites/default/files/public-files/assets/Neighbourhoods/NeighbourhoodProfile_Grovenor.pdf' target='_blank'>Photo by the City of Edmonton, 2021</a>."}
		caption={"The Grovenor neighbourhood in Edmonton provides examples of duplex and low-rise development in a mature setting."}
		maxWidth="680px"
		link='No'
	/>

	<div class="text">

		<p>
			However, zoning alone is not enough: growth also depends on street-level design, including active frontages, pedestrian-friendly streetscapes, and street reconfigurations that prioritize walking, cycling, and transit use. Permissive, progressive zoning for housing often prioritizes speed and quantity over coordination with existing infrastructure and public realm improvements. To be effective, zoning must be paired with social infrastructure, retail, and public amenities.<Footnote id={addFootnote(fns[8])}/>  Focusing medium-density infill along arterials and prominent corner lots concentrates activity where infrastructure and transit access are strongest, rather than dispersing it along neighbourhood edges.
		</p>

		<Recommendation count=2 title="Prioritize active transportation and transit and discourage driving"/>

		<p>
			Improving pedestrian and cycling connectivity around McKernan-Belgravia can strengthen access to the LRT station while supporting local trips without a car. Safe, seamless east-west pedestrian and cycling routes could transform 114 Street into a promenade linking the two university campuses, while 76 Avenue connects the neighbourhoods to nearby parks and open space along the North Saskatchewan River.
		</p>
	
	</div>

	<ImageMultiples
		images={[{url: "../web-assets/case-study/mckernan-belgravia/ualberta1.jpg"},
		 		{url: "../web-assets/case-study/mckernan-belgravia/ualberta2.jpg"}]}
		mainSource={"Photo by the University of Alberta."}
		mainCaption={"McKernan-Belgravia sits between the University of Alberta's North and South Campuses on the LRT. They anchor significant employment hubs for healthcare and education."}
		maxWidth="360px"
	/>

	<div class="text">

		<p>
			Transit quality itself is equally important. Research shows that the greatest TOD benefits occur when transit improvements meaningfully reduce travel times near higher-density development and enhanced amenities.<Footnote id={addFootnote(fns[9])}/>  Common barriers to positive transit experiences are poor transit service, unaffordable fares, and safety concerns. In Edmonton’s case, safety is the lowest-rated aspect of service, with only 62% of respondents reporting feeling safe during their journey.<Footnote id={addFootnote(fns[10])}/>  Among non-users, personal safety remains a significant reason for avoiding transit altogether. Continuing to prioritize safety measures can improve perceptions of reliability and comfort across the system while boosting ridership among new and existing residents alike.<Footnote id={addFootnote(fns[11])}/> 
		</p>

		<p>
			To reinforce a shift toward transit, policies must also disincentivize driving. Research shows that minimum parking standards have historically resulted in oversupply, encouraging vehicle ownership and driving while taking space that could be used for green space or infrastructure for active modes.<Footnote id={addFootnote(fns[12])}/>  Parking subsidies – particularly free or underpriced off-street parking – have been shown to distort travel behaviour and land use decisions by encouraging driving over more sustainable modes.<Footnote id={addFootnote(fns[13])}/> 
		</p>

		<p>
			Edmonton has already taken an important step by eliminating minimum parking requirements for new development. Additional parking management tools – such as charging for on-street parking – can further discourage car reliance, thereby improving accessibility to destinations, reducing congestion, and enhancing pedestrian and cyclist safety. Traffic management measures such as reduced vehicle speeds, limited through-movement, and transit priority treatments should be used to discourage cut-through traffic. Together, these measures help ensure that investments in transit and active transportation are supported by policies that meaningfully shift travel behaviour. 
		</p>

		<Recommendation count=3 title="Address public concerns and building support for infill"/>

		<p>
			In mature neighbourhoods like McKernan-Belgravia, the success of infill depends as much on social acceptance as on physical design. Given the scale of reforms introduced in the recent years, city staff must be mindful of pacing and public readiness for change. Planning operates within a political environment, and the way reforms are sequenced and communicated can shape the mandate for future policy direction. Advancing controversial or unpopular changes in this context can consume significant time and political energy while yielding only relatively modest gains in overall density.
		</p>

		<p>
			Recent ambiguity about the height, form, and the number of mid-block infill units permitted, with city staff and elected representatives on opposite sides of recommendations, has created uncertainty about how and when to engage for both community members and developers. Some residents also feel that their input is not fully considered, contributing to lower trust in municipal decision-making that makes it difficult for city staff to capture broad, representative input. 
		</p>

		<p>
			Best practices emphasize compatibility with existing neighbourhood character through meaningful participation among all targeted groups, strong public-private partnerships, improved public space, and continuous monitoring and evaluation of infill projects.<Footnote id={addFootnote(fns[14])}/>  Effective engagement requires grounding conversations in resident values rather than abstract growth targets. Framing infill around priorities such as aging in place and enabling families to remain in their communities can build trust, increase local ownership, and improve receptiveness to change.<Footnote id={addFootnote(fns[15])}/> 
		</p>

		<p>
			Managing the pace and perception of change is equally important. Different demographic groups experience neighbourhood change differently, and engagement processes should acknowledge these varied perspectives. Well-designed public engagement exercises create opportunities to build shared understanding, support behavioural shifts, and strengthen residents’ sense of responsibility for both the process and its outcomes.<Footnote id={addFootnote(fns[16])}/>  Consideration of these factors will ensure that infill is not only physically compatible but socially accepted, resilient, and sensitive to changing demographics.
		</p>

	</div>

	<ImageMultiples
		images={[{url: "../web-assets/case-study/mckernan-belgravia/vision2050_adults.jpg"},
		 		{url: "../web-assets/case-study/mckernan-belgravia/vision2050_kids.jpg"}]}
		mainSource={"Photos by the City of Edmonton, 2018."}
		mainCaption={"The City of Edmonton conducted extensive public engagement for the Vision 2050 Plan."}
		maxWidth="1080px"
	/>

	<div class="text">

		<p>
			The path forward is apparent: policy should incentivize high-quality development near the station more attractive than ad hoc infill, while actively deterring vehicle dependence. Though the direction is simple, implementation is complex – it requires weaving together refinements in built form, traffic management, and streetscape design that ensures the seamless movement of people. At the same time, highly prescriptive zoning can circumscribe the market to produce less housing than ad hoc infill, which can proceed whenever lots become available. Balancing intentional guidance with an understanding of market realities is essential to ensure both coordinated growth and sufficient housing supply. 
		</p>

		<p>
			Finally, community acceptance often grows over time: residents who initially resist change may come to appreciate improvements such as better public spaces, active transportation infrastructure and nearby amenities once the tangible benefits of development are realized. This strategic pivot is how the current plan’s initial community-informed objectives may be realized. 
		</p>

	</div>

	<ImageSingle
		imageURL={"../web-assets/case-study/mckernan-belgravia/edmonton_skyline.jpg"}
		source={"<a href='https://commons.wikimedia.org/wiki/File:Edmonton,_AB.jpg' target='_blank'>Photo by Quintin Soloviev, 2024</a>."}
		caption={"Edmonton's skyline."}
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
