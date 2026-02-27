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
	import GraphicMultiples from '$lib/GraphicMultiples.svelte';
	import Footer from '$lib/Footer.svelte';
	import FadingImages from "$lib/FadingImages.svelte";
    import ScrollAnimate from '$lib/ScrollAnimate.svelte';
	import Password from '$lib/Password.svelte';

	import topImage from './assets/NF_Background Frame_1.png' 

	import { createFootnoteStore } from '$lib/footnoteUtils';
    import { resolveRoute } from '$app/paths';
    import HamburgerMenu from '$lib/HamburgerMenu.svelte';

	export let data;

	import LogoBody from '$lib/LogoBody.svelte';
	import CaseStudyNote from '$lib/CaseStudyNote.svelte';
	import Footnote from '$lib/Footnote.svelte';
	import Footnotes from '$lib/Footnotes.svelte';
    import Recommendation from '$lib/Recommendation.svelte';
	const footnoteStore = createFootnoteStore();
	const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		'Region of Waterloo, <i>Monitoring Change in the CTC: 2025 Report</i>, no. 5057267 (2025), <a href="https://pub-regionofwaterloo.escribemeetings.com/filestream.ashx?DocumentId=15000" target="_blank">URL</a>',
		'Region of Waterloo, <i>Community Building Strategy</i> (2014), <a href="https://www.regionofwaterloo.ca/en/doing-business/resources/Community-Building-Strategy/Station_Area_Snapshots-Chapter_5.pdf" target="_blank">URL</a>, p. 122-123',
		'Robert Cervero, <i>Ridership Impacts of Transit-Focused Development in California (Working Paper No 176)</i>, 1993, <a href="https://escholarship.org/uc/item/8sr9d86r" target="_blank">URL</a>',
		'Jed Kolko, <i>Making the Most of Transit: Density, Employment Growth, and Ridership around New Stations</i> (2011), <a href="https://www.ppic.org/wp-content/uploads/content/pubs/report/R_211JKR.pdf" target="_blank">URL</a>',
		'Kevin Credit, “Transit-Oriented Economic Development: The Impact of Light Rail on New Business Starts in the Phoenix, AZ Region, USA,” <i>Urban Studies</i> 55, no. 13 (2018): 2838–62, <a href="https://doi.org/10.1177/0042098017724119" target="_blank">DOI</a>; Kolko, “Making the Most of Transit.”',
		'Jed Kolko, <i>Making the Most of Transit: Density, Employment Growth, and Ridership around New Stations</i> (2011), <a href="https://www.ppic.org/wp-content/uploads/content/pubs/report/R_211JKR.pdf" target="_blank">URL</a>',
		'Credit, “Transit-Oriented Economic Development”; Daniel G. Chatman et al., “Firm Births, Access to Transit, and Agglomeration in Portland, Oregon, and Dallas, Texas,” <i>Transportation Research Record</i> 2598, no. 1 (2016): 1–10, <a href="https://doi.org/10.3141/2598-01" target="_blank">DOI</a>',
		'Jeff Outhit, “Pedestrian Bridge Proposed over the Waterloo Expressway Dies before Its Time,” <i>The Record</i>, April 10, 2024, <a href="https://www.therecord.com/news/waterloo-region/pedestrian-bridge-proposed-over-the-waterloo-expressway-dies-before-its-time/article_9512090a-8374-55c1-8cae-f814c5bd472d.html" target="_blank">URL</a>',
		'Carl Grodach and Nícolas Guerra-Tao, “Industrial Lands, Equity, and Economic Diversity: A Comparative Study of Planned Employment Areas in Melbourne, Australia,” <i>Urban Research & Practice</i> 16, no. 5 (2023): 689–705, <a href="" target="_blank">DOI</a>',
		'Region of Waterloo, “Advanced Manufacturing,” accessed February 20, 2026, <a href="https://www.regionofwaterloo.ca/en/doing-business/advanced-manufacturing.aspx" target="_blank">URL</a>',
		'Joe Pavia, “Why a Parcel of Land on Waterloo Region’s East Side Is Key to Community’s Future Economic Prosperity,” <i>CBC</i>, March 24, 2021, <a href="" target="_blank">URL</a>',
		'Toronto Board of Trade, <i>The Race for Space</i> (2023), <a href="https://bot.com/Resources/Resource-Library/The-Race-for-Space" target="_blank">URL</a>'
	];

	const credits = [
		{ role:"Research and writing", names:"Sarah Chan, Kathryn Exon Smith, Anika Reisha Taboy"},
		{ role:"Architectural renderings", names:"Daniel Lam, Phat Le"},
		{ role:"Maps and data visualization", names:"Jeff Allen, Polina Gorn, Isabeaux Graham"},
		{ role:"Web development", names:"Mieko Yao, Jeff Allen"},
		{ role:"Additional contributors", names:"An Pham, Carrie Zeng"}
	]

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

	<title>Northfield | School of Cities</title>

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
	<Password correctPassword="catcatmeow"></Password>
	<!-- Full page title example -->
	<div class="wrapper">
		<!-- Top stays visually on top -->
		<div class="top" style="opacity: {topOpacity}; pointer-events: {topPointer};">
			<TitleFullPage
				title="Northfield Station"
				topic="Case Study"
				location="Waterloo, ON"
				subtitle="How can we transform industrial land into a vibrant community that attracts – and keeps – jobs and talent?  "
				image={topImage}
				imageOpacity=1
				imageAltText="A photo"
				tintColour="black"
				tintOpacity=0.5
				titleFontColour="var(--brandWhite)"
				subtitleFontColour="var(--brandWhite)"
				authorText="Author Name, Author Name, Author Name"
				secondLogo="II"
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
				header={"NORTHFIELD STATION"}
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
				This case explores the importance of keeping employment uses near transit amid housing pressures. 
			</p>

			<CaseStudyNote style=3/>

			<!-- <h1 id="Menu_2">Why this matters </h1> -->
			
			<h2 id="Menu_2">
				Neighbourhood overview 
			</h2>
			<p>
				Kitchener-Waterloo is the smallest municipality in North America to have higher-level rail transit. The ION LRT line, which opened in 2019, is part of a long-standing regional strategy of re-urbanization to limit sprawl and preserve surrounding agricultural lands.  
			</p>

		</div>

		<GraphicSingle
			svg720={"../web-assets/case-study/northfield/Northfield-720map.svg"}
			svg360={"../web-assets/case-study/northfield/Northfield-360map.svg"}
		/>

		<div class="text">

			<p>
				Since the announcement of the ION, significant development has occurred along the corridor. This growth has been supported in part by reductions or eliminations in development charges at both the regional and municipal levels.<Footnote id={addFootnote(fns[0])}/> The assessed value of properties in the corridor doubled through 2024 and grew faster than in the surrounding region, indicating that both renovations and new developments are adding value to the area. 
			</p>
			<p>
				Kitchener-Waterloo is booming, and the Northfield Station area, on the northern edge of the City of Waterloo, is in the middle of a district formerly home to industrial production. Nestled between tech hubs and the city’s largest shopping mall, the station is anchored by nearby employment centres, including the Waterloo Innovation Park and the Waterloo Corporate Campus. The plan for this area is to capitalize on the talent pipeline from the University of Waterloo and Wilfrid Laurier University – just a few LRT stops away – to fuel emerging sectors in AI, quantum tech, and cybersecurity.  
			</p>

		</div>

		<GraphicSingle
			svg720={"../web-assets/case-study/northfield/northfield-land-use-720.svg"}
			svg360={"../web-assets/case-study/northfield/northfield-land-use-360.svg"}
		/>

		
		<div class="text">

			<p>
				The area around the station today is still employment-focused, and warehouses, office parks, and parking lots dominate, with few amenities and little green space. The large industrial parcels surrounding the station offer an opportunity: with fewer owners, it is easier to assemble large sites for development. This is why many station areas in Canada, Australia, and the U.S. are seeing the conversion of formerly industrial lands into areas for residential and commercial development, which can generate more income. 
			</p>
			<p>
				There is currently little housing built in the area, which is mostly older detached homes and a few apartment buildings clustered on the western periphery. Existing residents are young and diverse. Nearly two-thirds are renters. With an average annual household income of $84,200 – well below the regional average – these are early-career workers and single-parent families with modest incomes.  
			</p>

		</div>

		<GraphicMultiples
			svgPaths={[
				"../web-assets/case-study/northfield/Northfield-population.svg",
				"../web-assets/case-study/northfield/Northfield-housing.svg",
				"../web-assets/case-study/northfield/Northfield-commuters.svg",
				"../web-assets/case-study/northfield/Northfield-income.svg"
			]}
		/>

		<div class="text">

			<p>
				Transit ridership on the LRT and in the region has risen faster than population growth since the system opened in 2019, reflecting planning decisions that encourage dense development in the core to build up a base of potential riders. But Northfield is still a car-oriented district: nearly 80% of commuters here drive. 
			</p>
			<p>
				Building on the city’s major transit investment, Northfield can become a thriving community with a mix of employment uses to drive transit ridership and social infrastructure – schools, parks, and retail – that will sustain a community of residents.   
			</p>

			<h1 id="Menu_3">Northfield’s current trajectory</h1>

			<p>
				The Northfield Station area was initially envisioned as one of three key employment nodes on the line with a “Business Employment” land use designation and little change anticipated in the amount of residential.<Footnote id={addFootnote(fns[1])}/> However, the region has experienced explosive growth in recent years, and the province has issued a directive to focus housing growth near transit, with a target for Northfield of 160 people and jobs per hectare – three times its current density.  
			</p>
			<p>
				This prompted the City to create a new zoning category for Northfield and the neighbouring Research & Technology Station – “Station Area Mixed Use” (SAMU) – that permits developments up to 30 storeys provided these retain space for mixed-use employment.  
			</p>

		</div>

		<ImageSingle 
			imageURL='../web-assets/case-study/northfield/nf_frame_8_current_dev_ink_edit.png'
			link='No'
			caption="Currently proposed or under construction development 800m from Northfield station."
			source="Infrastructure Institute (2025)."
			maxWidth="680px"
		/>

		<ImageSingle 
			imageURL='../web-assets/case-study/northfield/nf_frame_7_samu_ink_edit.png'
			link='No'
			caption="Land zoned as Station Area Mixed Use (SAMU) near Northfield station."
			source="Infrastructure Institute (2025)."
			maxWidth="680px"
		/>

		<div class="text">

			<p>
				The impact of this zoning change has been immediate. One proposal calls for 13 high-rise residential towers, which would add over 4,200 units and 21,000 square feet of commercial space.  
			</p>
			<p>
				If development continues in this way, Northfield Station will become a cityscape of glass towers. This would hit density targets but, without proper social infrastructure, the area could turn into a series of islands with internal amenities but disconnected from one another and the community.  
			</p>
			<p>
				Because successful TOD depends on locating a mix of <i>both</i> residential and employment destinations near transit,<Footnote id={addFootnote(fns[2])}/> there is also a risk that removing valuable employment uses near the ION could reduce system-wide transit ridership. 
			</p>

			<h1 id="Menu_4">
				Optimized scenario: Creating a complete community 
			</h1>
			<p>
				The central challenge is this: How can cities build vibrant communities centred on a major employment hub? What kind of community attracts top talent to work and live – and makes them want to stay?  
			</p>

		</div>

		<ImageCompare
			imageURL1="../web-assets/case-study/northfield/current-trajectory.png"
			caption1=""
			source1=""
			buttonLabel1="Current trajectory"
			imageURL2="../web-assets/case-study/northfield/optimized-scenario.png"
			caption2=""
			source2=""
			buttonLabel2="Optimized scenario"
			maxWidth="900px"
			link='No'
		/>

		<GraphicSingle
			svg720={"../web-assets/case-study/northfield/render-legend-720.svg"}
			svg360={"../web-assets/case-study/northfield/render-legend-360.svg"}
		/>

		<div class="text">	

			<Recommendation title="Incentivize ridership through a mix of employment uses"
			count=1/>
			<p>
				As the city’s zoning recognizes, keeping employment uses near transit stations is essential. These uses enable commuters to travel between home and work via transit, boosting regional transit mode share overall. Employment uses also support population targets and increase land values through higher rents. 
			</p>
			<p>
				But transit alone is not enough. Studies show that the presence of and densification around new stations does not automatically result in employment growth – TOD zones often need additional development incentives to attract a mix of businesses.<Footnote id={addFootnote(fns[3])}/> Retail and services, in particular, can kick-start a virtuous cycle of employment growth as employers cluster around amenities that their employees value.<Footnote id={addFootnote(fns[4])}/>  
			</p>
			<p>
				Access to everyday amenities around Northfield Station, such as grocery stores, child care, and health care, is currently well below the city average. Incentivizing these early would benefit both existing residents and future employers. Limiting parking near the station would further encourage active uses and transit ridership. 
			</p>
			<p>
				Distance to the station matters too, especially for workplaces. As the area transitions from flexible industrial zoning intended for light industrial uses to permit more premium, amenity-rich Class A office space and residential development, locating employment uses as close as possible to the station helps maximize ridership. Studies show that access to transit matters more to workers than residents, with ridership dropping off faster,<Footnote id={addFootnote(fns[5])}/> and many employees are reported to be unwilling to walk further than 400 metres from a station to work.<Footnote id={addFootnote(fns[6])}/> 
			</p>
			<p>
				Our optimized scenario uses a variety of building forms to create a sense of community at a human scale. Instead of isolated towers, density is spread horizontally. Towers remain clustered near the LRT – where intensity belongs – while mid-rise buildings everywhere else create a gentle transition to surrounding neighbourhoods.  
			</p>
			<p>
				Mid-rises also support street-level jobs and active storefronts. These elements strengthen the public realm, improve walkability, and enhances community life.  
			</p>

			<Recommendation title="Invest in connectivity to the station to boost transit use "
			count=2/>

			<p>
				Simply having a transit station, even one with frequent service, is not enough to drive high ridership. The station must be well connected to surrounding neighbourhoods, with easy access for both pedestrians and cyclists. 
			</p>
			<p>
				The Northfield Station area today is not very walkable: a third of its streets are missing sidewalks; a four-lane highway (the Conestoga Parkway) severs the district in two; no bike lanes connect directly to the station; and the platform itself is isolated, surrounded by parking lots, bordered by fences, and accessible only from a busy intersection next to a highway on-ramp.  
			</p>
			<p>
				These barriers send a clear message: driving is easier than transit. Without fixing these broken connections, new residents and workers will continue to choose their cars. Northfield risks becoming a “transit–adjacent” community – dense but disconnected.  
			</p>
			<p>
				In line with City guidance, improving connectivity means breaking down large, industrial super-blocks into a finer-grained street network. Smaller blocks, complete with linear parks, public open spaces, and mid-block pathways, are all important steps toward walkability. It also means creating a web of new active transportation links by removing fences and connecting the fragmented bike network. 
			</p>
			<p>
				The province should also reconsider its determination that improved pedestrian access – in the form of a bridge across the highway – is unnecessary.<Footnote id={addFootnote(fns[7])}/> Travelling via Northfield Drive is indirect, and the existing sidewalk and bike lanes on the Northfield Drive bridge are narrow and insufficient for existing capacity. A new or improved bridge here would do more than just move people – it could become a public space that finally unites Northfield’s two halves. 
			</p>
			<p>
				Stronger connections would benefit more than just the immediate community. Positioned on the northern edge of Waterloo, Northfield Station was envisioned by the City as a gateway and transit access point for the nearby Mennonite community and those travelling to and from neighbouring towns, including the local recreation and tourism destination of St Jacobs. Investing in stronger connections could also reduce driving and parking pressures in these areas. 
			</p>

		</div>

		<ImageSingle 
			imageURL='../web-assets/case-study/northfield/site-visit.jpg'
			link='No'
			maxWidth="680px"
			caption="Northfield Station has few access points for cyclists and pedestrians."
			source="Photo by Sarah Chan."
		/>

		<div class="text">


			<Recommendation title="Preserve industrial and commercial land with regional planning"
				count=3/>
			<p>
				The province and the region must work together to ensure the sufficient availability of employment lands – areas zoned specifically for industrial, commercial, institutional, and office uses and not mixed-use residential. While the Northfield Station area is a designated Provincially Significant Employment Zone, most current proposals are for housing.  
			</p>
			<p>
				As lands around station areas are re-zoned, preserving flexibility of uses is essential to prevent industrial displacement. Without it, rising land values could push out existing industrial and commercial tenants as they are no longer able to afford lease renewals or lose the space to expand.<Footnote id={addFootnote(fns[8])}/> Over time, this can lead to the gradual displacement of the jobs the region depends on. 
			</p>
			<p>
				This matters because Waterloo is a global hub of technology and advanced manufacturing –manufacturing is still the largest industry in the Region of Waterloo, employing a sixth of the population.<Footnote id={addFootnote(fns[9])}/> While the region has set aside large tracts of industrial land on the east near the Waterloo Regional Airport and Highway 401, these areas are difficult to reach by transit.<Footnote id={addFootnote(fns[10])}/> 
			</p>
			<p>
				Preserving employment land near stations like Northfield is not about choosing jobs over housing – it's about planning for both, so the region can grow sustainably.  
			</p>
			<p>
				When employment lands remain transit-accessible, local firms gain certainty about where they can grow by factoring in how their employees can get to work. Preserving employment lands in strategic locations also strengthens the economic competitiveness of the broader Golden Horseshoe region that Waterloo sits in, through providing places for reshoring to shorten supply chains, leading to greater economic independence.<Footnote id={addFootnote(fns[11])}/> 
			</p>
			<p>
				In our optimized scenario, existing industrial sites northwest of the station remain dedicated employment areas – now with better connectivity. This approach protects current manufacturing workers from displacement while fostering entrepreneurial activity in emerging tech sectors that require light-industrial space. These employment uses are not compatible with residential uses. Elsewhere in the station area, however, modern office spaces can be easily integrated with mixed-use development. Together, this mix of employers support a vibrant station area and gives workers the opportunity to live near family by taking transit to work. 
			</p>

			<p>
				Like many new transit station areas, Northfield is a place of opportunity: larger parcels allow for flexible development, and the area can accommodate more density in both jobs and housing. By weaving together tasteful density with new streets, connections, and the amenities people need to thrive, it transforms from an industrial zone into a thriving community.  
			</p>

		</div>
		
			
		<ImageSingle 
			imageURL='../web-assets/case-study/northfield/city-photo.png'
			link='No'
			maxWidth="680px"
			caption="A mix of uses, like the employment and retail shown here along King Street, will contribute to the success of transit investments like the ION in Waterloo Region."
			source="Photo source: <a href='https://www.waterlooedc.ca/' target='_blank'>Waterloo EDC.</a>"
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
