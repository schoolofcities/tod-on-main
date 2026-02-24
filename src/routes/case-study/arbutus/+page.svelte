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

	import topImage from './assets/AB_Background Frame_1.png' 

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

	<title>Arbutus | School of Cities</title>

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
				title="Arbutus Station"
				topic="Case Study"
				location="Vancouver, BC"
				subtitle="How can we preserve the best features of established neighbourhoods while increasing density around transit?"
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
				secondLogo="II"
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
				header={"ARBUTUS STATION"}
				imageAlign={"center"}
				imageWidth={"100%"}
				imageHeight={"100dvh"}
				textSectionMaxWidth={"400px"}
				textSectionAlign={"left"}
				fadeDuration={1200}
				mobileTextAlign={"top"}
				backgroundColour={"#F8F8F8"}
				bind:arrowColour
			/>
		</div>

	</div>


	<div class="text">
		<h1 id="Menu_2">Why this matters </h1>
		<p>
			When it opens in 2027, Arbutus Station at the end of the Broadway Line will be a prominent example of ambitious transit-oriented development in a well-established neighborhood. The station is intended to support seamless multimodal travel and enhance connections to the Arbutus Greenway. This area is in many ways already a complete community, and the challenge will be ensuring the area’s affordable housing stock and many amenities keep pace with densification, so it can continue to be a home for people of all income levels.  
		</p>
		<p>	
			A core strategy must tackle valid concerns around social disruption: the threat of displacement, perceived incompatibility of uses, and risks of delayed housing and amenity delivery. 
		</p>
		<h2 id="Menu_3">
			Neighbourhood overview 
		</h2>
		<p>
			Located in Vancouver’s Kitsilano neighbourhood, Arbutus Station is an established area with more than 30,000 residents. The community is diverse: one-third are immigrants and another quarter come from outside the province. This diversity contributes to a wide range of housing needs and service demands. 
		</p>
		<p>
			This area is largely built out, with over 80% of its structures built more than 25 years ago.  
		</p>
		<p>
			Low-rise apartment units make up 775% of the households within an 800-metre radius of the station, forming the backbone of the neighbourhood’s rental stock. These older rental apartments provide naturally occurring affordable housing (NOAH), but are increasingly vulnerable to redevelopment pressures as the area densifies.4 
		</p>
		<p>
			This vulnerability is reinforced by the area’s tenure profile: 57.1% of households rent, well above the national average of 46.8%. Most residents in these units are young to middle-aged professionals living alone. Houses, while very expensive due to the area’s prime location, make up just 8% of households.  
		</p>
		<p>
			Arbutus has a vibrant main street with a wide variety of retail and services, supporting a strong local economy and steady foot traffic. 
		</p>
		<p>
			However, there are gaps in community-serving amenities such as community centres, convenience stores, and particularly libraries. Residents are also concerned that essential public services, including parks and schools, may not keep pace to serve the rapid population growth. 
		</p>
		<p>
			Supporting equitable growth here involves balancing redevelopment with the needs of current residents and the broader community. 
		</p>

		<h2 id="Menu_4">
			Arbutus’ current trajectory 
		</h2>

		<p>
			The City’s Broadway Plan provides a 30-year vision for Arbutus, outlining growth, transit-oriented development, and mixed-use intensification in the station area.  The plan uses tools such as mass rezoning and Below Market Rate (BMR) rental requirements to guide development while integrating public spaces and amenities. 
		</p>

		<p>
			Implementation is already underway: over 14 proposals, mostly 20-30 storey towers, are moving through the rezoning process. Many of these projects meet the mandated policy of at least 20% BMR rental units.  
		</p>

		<p>
			If trends continue, the area could see approximately 7,000 new units, including more than 1,400 BMR units, nearly 10,000 new residents, and 1,700 new jobs. Early successes include meeting housing supply and affordability targets, along with planning for new public spaces and a vibrant public realm.  
		</p>

		<p>
			The Broadway Plan also includes robust anti-displacement measures. In 2022, City Council approved enhanced tenant protections under the Broadway Plan, in addition to the City-wide Tenant Relocation and Protection Policy (TRPP). These policies provide rent top-ups, moving cost coverage, relocation support, additional assistance for low-income tenants, the right to return at protected rents, and financial compensation of up to 24 months’ rent.5,6  
		</p>

		<p>
			To support implementation and oversight of these requirements, the City has committed to quarterly monitoring and reporting on tenant impacts.7 The City has also published a Tenant Relocation and Protection Policy Best Practices Guide for developers or property owners of existing rental buildings.8  
		</p>

		<p>
			Recognizing that redevelopment can also disrupt commercial activity, the City has introduced measures to support local businesses. These include a Mitigation Team, wayfinding programs, public art initiatives, and business awareness campaigns.9,10 
		</p>

		<p>
			While these policies are strong, implementation gaps remain. Mass rezoning designed to expedite housing delivery has been linked with speculation that drives up land values, which could undermine affordability. Higher-cost land could also force higher densities simply to meet mandated affordable unit targets. Similarly, reducing reliance on site-specific public hearings has prompted concerns about an erosion of democratic participation. 
		</p>

		<p>
			Long-term renters are especially vulnerable. NOAH renters – predominantly low-income people of colour – often live in these older, low-rise buildings that are primary targets for redevelopment.11 Delays between tenant evictions and the completion of replacement units, combined with inconsistent enforcement of tenant protection policies, have heightened fears of displacement. 
		</p>

		<p>
			Even with strong affordability requirements, policy and real estate trends suggest that these older rental buildings will continue to be systematically targeted for replacement by new mixed-use residential towers.  This is a common challenge in many TOD areas, where planners must balance growth, housing supply, and affordability while preserving existing NOAH for long-term tenants.  
		</p>
		
		<h2 id="Menu_5">
			Optimized scenario 
		</h2>

		<p>
			What improvements could be made to an already robust City plan to better support equitable outcomes as redevelopment accelerates?  
		</p>

		<p>
			To offer a contrast to the current trajectory, we created an “optimized” scenario that refines the City’s existing vision for the area by strengthening its spatial logic – focusing on where growth should be concentrated, and how it should transition into surrounding neighbourhoods. The optimized scenario reinforces Broadway and Arbutus Street as active, mixed-use corridors and key destinations.  
		</p>

		<p>
			Density is strategically layered outwards from these corridors, aligning height and intensity with transit access and surrounding residential areas. This approach supports active modes and transit use while directing growth more effectively. 
		</p>

		<h2 id="Menu_6">
			Advancing an equity-centred TOD approach
		</h2>

		<p>
			The Broadway Plan provides a strong foundation for transit-oriented growth, combining streamlined approvals with clear affordability and tenant protection requirements. The primary concerns are less about what is being built and more about how it is being delivered. Rather than reworking the Plan’s approach, the focus here is on targeted refinements that strengthen equity outcomes as implementation advances.  
		</p>

		<p>
			To structure this approach, recommendations are organized using the 3Ps framework – Production, Preservation, and Protection.12  
		</p>

		<h3>
			Recommendation 1: Continue production of new housing 
		</h3>

		<p>
			Increasing housing supply remains essential to meeting housing targets and advancing affordability. Research shows that adding new housing – both market rate and affordable – can help reduce rents by increasing overall supply, while creating opportunities to deliver affordable units on- or off-site.13 In many cases, the number of new affordable units produced through redevelopment can exceed and offset displacement associated with the new developments.14 
		</p>

		<p>
			Carefully designed density has been shown to coexist with liveable, sustainable neighbourhoods, supporting both housing supply and overall quality of life. Vancouver already has a long track record of delivering successful medium-density communities.15 
		</p>

		<p>
			Our optimized scenario concentrates higher-density, mixed-use development along Broadway, where commercial activity and transit access are already strongest. Focusing taller buildings and active ground-floor uses in these areas maximizes housing production while retaining the qualities cherished in neighbourhoods like Kitsilano.  
		</p>

		<p>
			Density then transitions step-wise into adjacent areas. Larger mid-rises are concentrated in existing apartment areas north of the station, with a gradual reduction in scale toward more modest infill in low-density areas to the south. This layered approach allows growth to be absorbed incrementally while maintaining neighbourhood livability. 
		</p>

		<p>
			Concentrating the greatest density closest to the station strengthens transit-oriented outcomes. Locating more residents and jobs within walking distance of rapid transit improves access to daily services, supports higher ridership, and enables more people to live and work near high-capacity transit. 
		</p>

		<h3>
			Recommendation 2: Preserve existing affordable housing and neighbourhood stability 
		</h3>

		<p>
			Preserving existing NOAH is critical to advancing equitable TOD, particularly in the early stages of redevelopment. The loss of older rental housing through disrepair or redevelopment not only accelerates displacement, but also represents a missed opportunity to support long-term wealth creation in marginalized communities.16 
		</p>

		<p>
			As redevelopment accelerates, preservation should be treated as a core component of the City’s housing strategy rather than a secondary outcome. One opportunity is to explicitly recognize and track the supply of NOAH in affordable housing targets, ensuring that the retention of existing affordable units is considered alongside the production of new ones.17 
		</p>

		<p>
			The City can also support reinvestment in existing rental buildings. Offering grants and low-interest loans for upgrades and repairs would help address a key driver of NOAH loss: deferred maintenance and limited access to capital. Preventative reinvestment can extend the life of existing buildings, improve living conditions for tenants, and reduce pressures to sell or redevelop prematurely.18 
		</p>

		<p>
			This theme can also extend to the preservation of neighbourhood stability and trust as density increases.  
		</p>

		<p>
			While mass rezoning is an essential tool to expedite housing delivery, long-term success depends on trust built through public engagement. Rather than relying on site-specific negotiations, neighbourhood-level design standards – developed through meaningful, upfront consultation – could be integrated into pre-zoning frameworks. 
		</p>

		<p>
			Best practices in sustainable urban development emphasize that context-sensitive design and participatory planning are key to balancing growth with place-making and equity objectives. Vancouver’s experience shows that achieving this requires collaboration between politicians, developers, city planners, and local community members to craft locally responsive solutions.19 
		</p>

		<p>
			Attention to land use compatibility is essential in a diverse station area such as Arbutus. Identifying and thoughtfully managing potentially incompatible uses near sensitive community assets can help prevent conflict, reduce opposition to new development, and support a safe, inclusive environment for everyone to thrive. 
		</p>

		<h3>
			Recommendation 3: Protect current residents 
		</h3>

		<p>
			Government policies can help ensure residents stay in place as neighbourhoods densify. Research shows that neighbourhood stabilization strategies are more effective at preventing direct displacement than housing production and preservation, which primary address indirect or exclusionary displacement.20  
		</p>

		<p>
			While the Broadway Plan includes strong protections under the TRPP, implementation gaps limit its effectiveness. Protections such as rent top-ups, relocation support, and the right to return at protected rents are vital, but the lack of a dedicated enforcement body reduces accountability. Without a clear mechanism to ensure compliance, long-term renters remain vulnerable. 
		</p>

		<p>
			To address these gaps, the City should guarantee pathways for both temporary and permanent housing for tenants affected by redevelopment, and ensure that enforcement is proactive rather than reactive. This allows policymakers to respond to emerging pressures and adjust displacement strategies accordingly. 
		</p>

		<p>
			The current trajectory’s core direction is sound: density and speed are essential to building housing supply.   
		</p>

		<p>
			The path is not to slow growth, but to strengthen the process. Successful, equitable TOD depends on balancing new development with the protection of existing residents, affordability, and neighbourhood stability. 
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
