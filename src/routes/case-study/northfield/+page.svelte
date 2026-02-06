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

	import topImage from './assets/NF_Background Frame_1.png' 

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
	<Password correctPassword=""></Password>
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
		

			<!-- <h1 id="Menu_2">Why this matters </h1> -->
			<p>
				Employment uses are an important part of complete communities, and locating jobs near transit drives ridership. In Kitchener-Waterloo, a successful LRT project has spurred significant development in a region with strong employment growth. Northfield Station offers an opportunity to grow ridership by building on large, formerly industrial parcels and planning for a connected community with a mix of forms and uses. This case explores the importance of keeping employment uses near transit amid housing pressures. 
			</p>
			
			<h2>
				Neighbourhood overview 
			</h2>
			<p>
				Kitchener-Waterloo is the smallest municipality in North America to have higher-level rail transit. The ION light rail transit (LRT) line, which opened in 2019, is part of a long-standing regional strategy of re-urbanization to limit sprawl and preserve surrounding agricultural lands.  
			</p>
			<p>
				There has been significant development along the ION corridor since its announcement, aided in part by reductions or eliminations in development charges at both the regional and municipal levels within core downtown growth nodes from 2011-2019.1 The assessed value of properties in the corridor doubled through 2024 and grew faster than in the surrounding region, indicating that both renovations and new developments are adding value to the area. 
			</p>
			<p>
				Kitchener-Waterloo is booming, and the Northfield Station area, on the northern edge of the City of Waterloo, is in the middle of a district formerly home to industrial production. Nestled between tech hubs and the city’s largest shopping mall, the station is anchored by nearby employment centres, including the Waterloo Innovation Park and the Waterloo Corporate Campus. The plan for this area is to capitalize on the talent pipeline from nearby universities – just a few LRT stops away – to fuel emerging sectors in AI, quantum tech, and cybersecurity.  
			</p>
			<p>
				The area around the station today is still employment-focused, and warehouses, office parks, and parking lots dominate, with few amenities and little green space. The large industrial parcels surrounding the station offer an opportunity: with fewer owners, it is easier to assemble large sites for development. This is why many station areas in Canada, Australia, and the U.S. are seeing the conversion of formerly industrial lands into areas for residential and commercial development, which can generate more income. 
			</p>
			<p>
				There is currently limited residential here, which is mostly older homes and a few apartment buildings clustered on the western periphery. Existing residents are young and diverse. Nearly two-thirds are renters. With a median annual household income of just $84,200 – well below the regional average – these are early-career workers and single-parent families with modest incomes.  
			</p>
			<p>
				Transit ridership on the LRT and in the region has risen faster than population growth since the system opened in 2019, reflecting planning decisions that direct density to the core to build up a base of potential riders. But Northfield is still a car-oriented district a district: nearly 80% of commuters here drive.  
			</p>
			<p>
				Building on the city’s major transit investment, Northfield can become a thriving community with a mix of employment uses to drive transit ridership and the amenities and social infrastructure - schools, parks, and retail - that will sustain a community of residents.   
			</p>
			<p>
				The School of Cities has created five case studies of different kinds of transit-oriented development across Canada to explore the opportunities and trade-offs involved in creating thriving communities near transit. In each case, we explore current patterns of growth and project what that community might look like in 20-30 years if development continues in this way (the current trajectory). We then explore an alternative, “optimized” scenario that imagines policy and design changes that could address key challenges. 
			</p>

			<h2>Northfield’s current trajectory </h2>
			<p>
				The Northfield Station area was initially envisioned as one of three key employment nodes on the line with a “Business Employment” land use designation and little forecast change in residential.2 However, the region has experienced explosive growth in recent years, and the province has issued a directive to focus housing growth near transit, with a target for Northfield of 160 people and jobs per hectare, three times its current density.  
			</p>
			<p>
				This prompted the city to create a new zoning category for Northfield and the neighbouring Research & Technology station - “Station Area Mixed Use” (SAMU) - that permits developments up to 30 storeys provided it retains space for mixed-use employment.  
			</p>
			<p>
				The impact of this zoning change has been immediate. One proposal calls for 13 residential towers reaching up to 40 storeys high. It would add over 4,200 units and 21,000 square feet of commercial space.  
			</p>
			<p>
				If development continues in this way, Northfield Station will become a cityscape of glass towers. This would hit density targets, but without proper social infrastructure, the area could turn into a series of islands with internal amenities but disconnected from one another and the community.  
			</p>
			<p>
				Because successful TOD requires a variety of both residential and employment destinations to be near transit,3 there is also a risk of removing valuable employment uses near the ION that could drive transit use across the system. 
			</p>

			<h2>Creating a complete community  </h2>
			<p>
				The central challenge is this: How can cities build vibrant communities centred on a major employment hub? What kind of community attracts top talent to work and live – and makes them want to stay?  
			</p>

			<h3>
				Recommendation 1: Incentivize ridership through a mix of employment uses 
			</h3>
			<p>
				As the city’s zoning recognizes, it is critical to preserve employment uses near transit stations. These ensure commuters can access home and work via transit, improving transit mode share in the region as a whole. Employment uses contribute to population targets while generating land value uplift through higher rents. 
			</p>
			<p>
				Yet studies of efforts to densify around new stations show that the existence of transit alone does not automatically lead to employment growth, and TOD zones may need additional development incentives to attract a mix of businesses.4 Retail and services can kick-start a virtuous cycle of employment growth as employers cluster around the kinds of amenities their employees want to access nearby.5  
			</p>
			<p>
				Access to core amenities like grocery stores, childcare, and health care is currently well below the city average, so incentivizing these early can benefit existing residents and future employers. Limiting parking in the station area will encourage active uses. 
			</p>
			<p>
				Proximity to the station is also important, especially for employment uses. As the area transitions from flex zoning to allowing more class A office space and residential, locating these uses adjacent to the station will maximize ridership, as studies show that the benefit of transit access drops off more quickly for business than for residential uses, and many employees are unwilling to walk further than 400 metres from a station to work.67 
			</p>
			<p>
				In our optimized scenario, a variety of building forms help to create a sense of community at a human scale. Instead of isolated towers, we distribute density horizontally. Towers remain, clustered near the LRT where intensity belongs, but elsewhere mid-rise buildings create a gentler transition to established neighbourhoods.  
			</p>
			<p>
				Mid-rises also create opportunities for employment uses and an active street front, further enhancing the public realm and walkability.  
			</p>

			<h3>Recommendation 2: Invest in connectivity to the station to boost transit use </h3>
			<p>
				Simply having a transit station, even one with frequent service, is not enough to drive high ridership. The station must be well connected to surrounding neighbourhoods, with easy access for both pedestrians and cyclists. 
			</p>
			<p>
				The Northfield Station area today is a difficult place to walk: a third of its streets are missing sidewalks. The Conestoga Parkway, a four-lane highway, severs the district in two. No bike lanes connect directly to the station. The platform itself is also isolated, surrounded by parking lots, bordered by fences, and accessible only from a busy intersection next to a highway on ramp. Without fixing these broken connections, new residents and workers will keep choosing to drive, and Northfield will become a “transit-adjacent” community – dense but disconnected.  
			</p>
			<p>
				In line with City guidance, better connectivity would involve developments that break down large, industrial super-blocks into a finer-grained network of smaller blocks complete with linear parks, public open spaces, and mid-block pathways, all important steps toward walkability. It also means creating a web of new active transportation links by removing fences and connecting the fragmented bike network. 
			</p>
			<p>
				The province must also reconsider its determination that improved pedestrian access – in the form of a new or improved bridge across the highway – is “unnecessary.”8 Travelling via Northfield Drive is indirect, and the existing sidewalk and bike lanes on the Northfield Drive bridge are narrow and insufficient for existing capacity. More than just a crossing, a better bridge here could become a public space that unites Northfield’s two halves for the first time.  
			</p>
			<p>
				These changes have the potential to benefit more than just the immediate community. Positioned on the northern edge of Waterloo, Northfield Station was envisioned by the City as a gateway and transit access point for the nearby Mennonite community and those travelling to and from neighbouring towns, including the local recreation and tourism destination of St Jacobs. Investing in stronger connections could also lessen the impact of driving and parking pressures in these areas. 
			</p>

			<h3>
				Recommendation 3: Preserve industrial and commercial land with regional planning 
			</h3>
			<p>
				The province and the region must work together to ensure the area has sufficient availability of employment lands -- that is, areas zoned for industrial, commercial, institutional, and office uses and not mixed-use residential. The Northfield Station area was designated a Provincially Significant Employment Zone but residential uses are now the majority of what is being proposed for the area.  
			</p>
			<p>
				As lands around station areas are re-zoned, it is essential to preserve a flexibility of uses to prevent potential industrial displacement. This can result from rising land values near transit, leading to firms not being able to afford to renew leases, or not having room to expand.9  
			</p>
			<p>
				Manufacturing is still the largest industry in the Region of Waterloo, employing a sixth of the population, and Waterloo is a global hub of technology and advanced manufacturing.10 The region has set aside a large area of land on the eastern edge of the region, near the major transportation nodes of the Waterloo Regional airport and Highway 401, as dedicated industrial space – but this is not easily accessible by transit. 
			</p>
			<p>
				Ensuring that local firms have stability in knowing where they can grow by ensuring employment land remains transit accessible for employees will provide options for firms. Preserving employment lands in strategic locations is also important for the economic competitiveness of the broader Golden Horseshoe region, as these areas provide places for reshoring to shorten supply chains and economic independence.11 
			</p>
			<p>
				In our optimized scenario, existing industrial sites northwest of the station remain employment areas -- now with better connectivity -- preserving access for industrial workers who are often displaced by TOD. While light industry and manufacturing can stay separate, modern office spaces are compatible with a mix of other uses. The mix of employers contributes to a vibrant station area and the opportunity for workers to live near family and work near transit. 
			</p>
			<p>
				Like many new transit station areas, Northfield is a place of opportunity: larger parcels offer flexible development potential, and the area can accommodate more density in both jobs and residences. By weaving together tasteful density with new streets, connections, and the amenities people need to thrive, it can transform from a place of work into a thriving community.  
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
