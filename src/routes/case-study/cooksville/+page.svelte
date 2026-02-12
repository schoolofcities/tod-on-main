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

	import topImage from './assets/cc_title.png' 

	import { createFootnoteStore } from '$lib/footnoteUtils';
    import { resolveRoute } from '$app/paths';
    import HamburgerMenu from '$lib/HamburgerMenu.svelte';

	export let data;

	import Footnote from '$lib/Footnote.svelte';
	import Footnotes from '$lib/Footnotes.svelte';
    import ImageMultiples from '$lib/ImageMultiples.svelte';
    import GraphicMultiples from '$lib/GraphicMultiples.svelte';
	const footnoteStore = createFootnoteStore();
	const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		'<a href="https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710015901" target="_blank">https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710015901</a>',
		'<a href="https://climateinstitute.ca/wp-content/uploads/2024/09/Fact-sheet_-Floods_CanadianClimateInstitute.pdf " target="_blank">https://climateinstitute.ca/wp-content/uploads/2024/09/Fact-sheet_-Floods_CanadianClimateInstitute.pdf</a>',
		'Link back to Prentiss',
		'Young Families and High-Rise: Towards Inclusive Vertical Family Housing',
		'<a href="" target="_blank"></a>'
	];

	const credits = [
		{ role:"Research and writing", names:"Sarah Chan, Kathryn Exon Smith"},
		{ role:"Renderings", names:"Daniel Lam, Phat Le"},
		{ role:"Data visualizations", names:"Jeff Allen"},
		{ role:"Web development", names:"Mieko Yao"},
		{ role:"Additional contributors", names:"Anika Reisha Taboy, Carrie Zeng"}
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

	<title>Cooksville | School of Cities</title>

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
				title="Cooksville Station"
				topic="Case Study"
				location="Mississauga, ON"
				subtitle="How can we build complete, family-friendly communities while managing flood risk? "
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

		<HamburgerMenu
		iconColour={arrowColour}
		contents={data.menuItems}/>

		<ScrollAnimate 
			colour={arrowColour}></ScrollAnimate>


		<!-- Bottom is underneath, scrolls normally -->
		<div class="bottom" id="before-text">
			<FadingImages
				sections={data.animations[0].items}
				header={"COOKSVILLE STATION"}
				imageAlign={"center"}
				imageWidth={"100%"}
				imageHeight={"100dvh"}
				textSectionMaxWidth={"400px"}
				textSectionAlign={"left"}
				fadeDuration={1200}
				mobileTextAlign={"top"}
				backgroundColour={"#FAFAFA"}
				bind:arrowColour
			/>
		</div>

	</div>


	<div class="text">
		

			<!-- <h1 id="Menu_2">Why this matters </h1>
			<p>
				Adding density around transit stations requires planning for different kinds of households. Over 35% of Canadian households contain three or more people, but much of the existing and planned housing near transit stations is designed for individuals or couples.<Footnote id={addFootnote(fns[0])}/>
			</p>
			<p>	
				Cities are also facing greater risks from a changing climate, with flooding the most frequent and costly impact across the country.<Footnote id={addFootnote(fns[1])}/> This case explores strategies for more inclusive densification while managing flood risk. 
			</p> -->
			<!-- INSERT: creek image -->
			 <p>
				<i>
					The School of Cities has created five case studies of different kinds of transit-oriented development across Canada to explore the opportunities and trade-offs involved in creating thriving communities near transit. In each case, we explore current patterns of growth and project what that community might look like in 20-30 years if development continues in this way (the current trajectory). We then explore an alternative, “optimized” scenario that imagines policy and design changes that could address key challenges.
				</i>
			</p>

			<h2 id="Menu_2">
				Neighbourhood overview 
			</h2>
			<p>
				The Cooksville neighbourhood in Mississauga is a future transit hub where the existing GO rail network will converge with the new Hazel McCallion light rail transit (LRT) and Dundas Bus Rapid Transit (BRT) lines, making it a focal point for growth.  
			</p>

		</div>

		

		<GraphicSingle
			svg720={"../web-assets/case-study/cooksville/cooksville-station-map-720.svg"}
		/>

		
		<div class="text">

			<p>
				The Cooksville station area also sits within the Cooksville Creek watershed, which is at risk of flooding in the event of significant storms. The City of Mississauga has undertaken significant stormwater management work in the area, including creating an upstream water storage pond, but high levels of development make this area – like many urban areas on floodplains – vulnerable to inundation.<Footnote id={addFootnote(fns[0])}/>
			</p>

			<p>
				With over 30,000 residents, Cooksville is dense, vibrant and diverse. Nearly 73% are visible minorities. A gateway for immigrants, two-thirds of Cooksville’s residents are foreign-born, and one in five is a recent arrival.  
			</p>

		</div>

		<GraphicMultiples
			svgPaths={[
				"../web-assets/case-study/cooksville/cooksville-population.svg",
				"../web-assets/case-study/cooksville/cooksville-income.svg"
			]}
		/>

		<div class="text">

			<p>
				Cooksville is young, with an average age of 37.4 and many families, alongside a growing number of seniors, of whom many live alone. Many people – especially renters -- live in high-rise apartments along the major corridors of Hurontario and Dundas Streets, but there are also established, lower-density neighbourhoods further from the station. 
			</p>
			<p>
				Household incomes average about $92,000 per year, far below the city average.  
			</p>
			<p>
				Seeing Cooksville as a high-potential node for growth, the City has set an ambitious future density target of 300 people and jobs per hectare for the station area. 
			</p>
			<p>
				Yet planning for inclusive growth here will require prioritizing the needs of current and future residents, particularly families. Many elements of successful complete communities are present, mainly centred on the “Four Corners” of Hurontario and Dundas -- schools, health care, and retail – but access to child care is limited, and the area has a critical gap in community centres
			</p>
			<!-- INSERT: visual -->
			<p>
				There is also little existing green space. With few formal civic amenities, residents rely on commercial plazas and small parks for daily needs. And like many suburban areas, the neighbourhood itself is built for the car: wide arterials and fragmented sidewalks make walking and cycling a challenge.  
			</p>
			<p>
				Another challenge comes from the site itself. Cooksville has over 300 buildings sitting on the Cooksville Creek floodplain, and the area has been deemed a flood risk. 
			</p>
	
		</div>

		<GraphicSingle
			svg1080={"../web-assets/case-study/cooksville/cooksville-flood-map-1080.svg"}
			svg720={"../web-assets/case-study/cooksville/cooksville-flood-map-720.svg"}
		/>

		<div class="text">

			<p>
				Creating a thriving community here will require creative approaches to managing risk while increasing access to critical amenities.  
			</p>
			
			<h1 id="Menu_3">
				Cooksville’s current trajectory 
			</h1>

			<p>
				A recent surge in investment and proposed development in the area as the Hazel McCallion line nears completion suggests developer confidence in Cooksville’s potential.<Footnote id={addFootnote(fns[2])}/> Dozens of high-rise projects are in the pipeline, set to transform surface parking lots and aging retail plazas into mixed-use towers. 
			</p>

		</div>

		<ImageSingle
			imageURL="../web-assets/case-study/cooksville/cooksville-current-dev.png"
			caption="Currently proposed or under construction development 800m from Cooksville station."
			source="Infrastructure Institute (2025)"
			maxWidth="680px"
			link='No'
		/>

		<div class="text">	

			<p>
				If growth continues this way, it will be concentrated on a handful of underused commercial and industrial lots. The default is towers on podiums – a built form tried and tested for effectively increasing density. 
			</p>

			<ImageMultiples
				images={[{url:"../web-assets/case-study/cooksville/Growth1.png", alt:"", caption:"asdf"},
							{url:"../web-assets/case-study/cooksville/Growth2.png", alt:"", caption:"asdf"}
				]}
				matchWidth={false}
				matchHeight={true}
			/>

			<p>
				New towers are clustered on fragmented lots, with density in the form of height to offset costly flood mitigation measures in basements and ground floors. 
			</p>

		<!-- </div>

		<ImageSingle
			imageURL="../web-assets/case-study/cooksville/cooksville-current-trajectory.png"
			caption="Current trajectory for development around Cooksville Station."
			source="Infrastructure Institute"
			maxWidth="680px"
			link='No'
		/>

		<div class="text"> -->

			<p>
				But this does not necessarily create a livable neighbourhood, and without early investment in civic infrastructure, Cooksville risks becoming just a collection of towers: dense but socially thin.    
			</p>

			<p>
				Crucial infrastructure is not keeping pace. The Cooksville Community Hub, co-located with the Thomas L. Kennedy Secondary School, is planned but needs funding. Other cultural amenities are virtually non-existent.  
			</p>

		</div>

		<ImageSingle
			imageURL="../web-assets/case-study/cooksville/cooksville-community-hub.jpg"
			caption="Rendering of the Cooksville Community Hub."
			source="SOURCE??? This was just in the project folder"
			maxWidth="680px"
			link='No'
		/>
		
		<div class="text">

			<p>
				Local parks are small and discontinuous, and few institutional sites exist to anchor future population growth.  
			</p>

			<p>
				Building a more complete community here requires more intentional planning – for families, and for floods. Here’s how we it could be done. 
			</p>

		</div>

		<ImageCompare
			imageURL1="../web-assets/case-study/cooksville/cooksville-scenario1.png"
			caption1=""
			source1="Infrastructure Institute, School of Cities (2025)."
			buttonLabel1="Current trajectory"
			imageURL2="../web-assets/case-study/cooksville/cooksville-scenario2.png"
			caption2=""
			source2="Infrastructure Institute, School of Cities (2025)."
			buttonLabel2="Mixed-use scenario"
			maxWidth="900px"
			link='No'
		/>

		<div class="text">	

			<h1 id="Menu_4">
				Building for families, building for all 
			</h1>

			<p>
				New mid- and high-rise construction is often oriented toward individuals or couples without children, even though families have always lived in these kinds of spaces.<Footnote id={addFootnote(fns[3])}/> Improving the number and kind of family-oriented units, with targeted community improvements, can increase density around transit and benefit all residents. 
			</p>
			

			<h3>
				Recommendation 1: Provide more 2- and 3- bedroom units
			</h3>

			<p>
				The best way to include families in growth is to give them the space they need. Cramped spaces and an insufficient number of bedrooms are the most common issues cited by both children and adults in high-rise dwellings.5 Units with two or more bedrooms allow more flexible space for families and multi-generational households.6 
			</p>

			<p>
				In Mississauga, two-thirds of households are families, but most proposed new buildings allocate 70% of units as studios or 1-bedrooms.  
			</p>

		</div>

		<GraphicSingle
			svg720={"../web-assets/case-study/cooksville/cooksville-scenario-comparison-720.svg"}
			svg360={"../web-assets/case-study/cooksville/cooksville-scenario-comparison-360.svg"}
		/>

		<div class="text">	

			<p>
				The market shows an appetite for more bedrooms: demand for 1-bedrooms is low, with supply outpacing demand. Meanwhile, even in the current slow condo market, many larger units are selling above asking price, with 2.5 times the sales volume.  
			</p>

			<p>
				Our research has shown that this is also a more efficient way to build because kitchens and bathrooms are shared by more people. This allows for a reduction in extreme height. Towers can be shorter, and more mid-rise buildings can be introduced to create active, human-scaled street fronts.  
			</p>

			<!-- CHART SHOWING % of GHG emission differences in 2 scenarios -->

			<p>
				Mississauga has already taken steps to incentivize this kind of unit mix by eliminating municipal development charges for units with 3 or bedrooms in purpose-built rental apartments.7 This incentive could be expanded by similarly eliminating these charges at the regional level, or for all new buildings. Other countries, such as Ireland, go further and prescribe a mix of apartment sizes and bedroom numbers before new developments are approved.8 
			</p>

			<h3>
				Recommendation 2: Adopt Canadian and global good practices at the site level 
			</h3>

			<p>
				In addition to the number of bedrooms, spaces within units must be flexible. Some cities, including Toronto in its Growing Up guidelines for vertical communities, suggest having a recommended play space of 2 by 3 metres within units. Guidelines such as these make planning for larger households more concrete. 
			</p>

			<p>
				Safety and connection are also essential, with many studies citing windows and balconies as areas that can often be improved with required safety mechanisms to make units more family friendly.9 Within buildings, ensuring that there are shared spaces, courtyards with play areas, and facilities that children can access – including elevator buttons at child level – encourages connection and independence. 
			</p>

			<p>
				Easy interaction with the street can mitigate a lack of private outdoor space, making density more appealing. In their design guidelines, cities can also ensure buildings are surrounded and green spaces with places to play (not solely planted gardens or inaccessible hardscape) away from busy roads.10 
			</p>

			<h3>
				Recommendation 3: Prioritize family-friendly retail and amenities in the surrounding area 
			</h3>

			<p>
				At the neighbourhood level, Canadian cities have long been leaders in setting guidelines for what services should be available nearby, from schools to transit stops to grocery stores.11 The optimized plan builds on this, integrating community theatres, youth centres, and libraries directly into new mixed-use blocks.   
			</p>

			<p>
				Like many people, families enjoy the benefits of compact urban living: proximity to jobs and schools, a diversity of people and stores, and cultural amenities like swimming pools.12 Ensuring child care and school amenities keep pace with density is a core element of growth. A mix of retail is important for all communities, but children specifically want outdoor space to play, inexpensive shops, and libraries, as young people use libraries at high rates.13 
			</p>

			<h1 id="Menu_5">
				Addressing rising flood risk 
			</h1>

			<p>
				The past 20 years have seen significant urban floods across Canada, including in Calgary, Winnipeg, Toronto -- and Mississauga, including one in 2024 that caused $$ of damage across the city.14 Southern Ontario in particular has been a site of increasing urbanization in areas of increasing flood exposure since 1985.15 As in many Canadian neighbourhoods, future growth in Cooksville will need to balance density with minimizing risk and flood exposure.  
			</p>

			<h3>
				Recommendation 1: Minimize impermeable surfaces and costly engineering through parcel selection 
			</h3>

			<p>
				The “tall and sprawl” model of urban growth – which features high-rise towers surrounded by lower-density, often single-family, homes – is often criticized, but in flood zones it can make sense. 
			</p>

			<p>
				Many properties east of Hurontario Street are regulated by the Credit Valley Conservation Authority, meaning that any development in this area must undergo strict flood mitigation to proceed. These guidelines incentivize taller growth on smaller footprints. 
			</p>
			<!-- INSERT: image -->
			<p>
				In part, this is because urbanization increases the area of impermeable surfaces, such as parking lots, roads, and buildings, where water cannot soak into the ground.16 Choosing sites that limit additional impermeable surface area decreases this risk. 
			</p>

			<p>
				Our optimized approach starts by adopting the current city strategy for where to build: on underused parcels, like aging plazas and surface parking lots. This leaves stable residential neighbourhoods mostly untouched.
			</p>

			<p>
				Accounting for floodplain considerations and preserving existing neighbourhoods, these are the parcels most eligible for development. 
			</p>

			<h3>
				Recommendation 2: Invest in multi-benefit green infrastructure 
			</h3>

			<p>
				Today, developers are engineering their way around the floodplain with elevated podiums, underground storage tanks, and on-site water detention systems. These “grey infrastructure” strategies are expensive and, buried below grade, invisible to the public eye.
			</p>

			<!-- INSERT: SIDE BY SIDE IMAGE -->

			<p>
				But what if we approached floodplain mitigation as an opportunity to improve public space? This moves beyond simply burying water tanks underground to lower flood risk through natural, “green” infrastructure such as parks and pathways, and design features that are a feature of development.17 
			</p>

			<p>
				By weaving this green infrastructure across sites, we create daily spaces for social connection: new pathways, parks, and adaptive landscapes that guide future development.  
			</p>

			<p>
				And the more developers who adopt this strategy, the larger the greenspace network, amplifying benefits for the entire community. 
			</p>

			<p>
				This multi-benefit infrastructure like this can be more expensive upfront because it often features layered built and landscape improvements, and therefore involves the time expertise of many people (such as engineers, ecologists, and architects).18  
			</p>

			<p>
				But it can increase the appeal of the area, and neighbouring property values.19 Cheonggyecheon Urban Park in South Korea combines public space with flood mitigation when needed, and has contributed significantly to the 30-50% increase in neighbouring land value.20 Green stormwater improvements in Philadelphia have increased nearby home values by 10%, which also contributes to the city’s tax base.21 
			</p>

			<h3>
				Recommendation 3: Maintain and improve current stormwater infrastructure, while prioritizing infill over sprawl 
			</h3>

			<p>
				Continued investment in stormwater infrastructure by all orders of government will be critical for Cooksville. Previous municipal efforts including an upstream stormwater pond helped to protect the neighbourhood from severe flooding in 2024,22 and the City has approved a $308-million stormwater management plan for the next decade.
			</p>

			<p>
				City-wide, more features like this, as well as increasing soil and vegetation that can absorb and filter water, will decrease the risk of overwhelming aging infrastructure, with the added benefit of decreasing contamination from fertilizers, pesticides, and roads that runs off into drains.23 
			</p>
			<!-- INSERT: IMAGE -->
			<p>
				Also critical will be minimizing new construction. Continuing to build in dense, TOD areas instead of in patterns of sprawl will slow new infrastructure build-out, and the costs associated with maintaining thousands of kilometres of pipes.24 
			</p>

			<h3>
				Recommendation 4: Develop more nuanced understanding of flood risk in TOD areas 
			</h3>

			<p>
				It is not just proximity to water that carries a flood risk, but how vulnerable people and assets are to exposure.25 Cooksville is considered a high-risk area in part because of social factors, including large populations of seniors and young children, high numbers of renters, lower incomes, and language barriers.26 
			</p>

			<p>
				The area also has more older building stock (built before 1980) than many neighbourhoods in Mississauga. These homes can have weaker foundations and less flood protection than newer construction. 
			</p>

			<p>
				In Cooksville, as in many neighbourhoods across the country, developing a comprehensive understanding of how built form and social vulnerability interact with flood risk geography can shape planning interventions such as building code changes, targeted incentives to repair, or zoning that incentivizes more concentrated development. 
			</p>

			<p>
				Social infrastructure, from the community hub to vibrant local shops, is woven into a landscape where green corridors double as flood protection and public parks.  
			</p>

			<p>
				By treating housing, amenities, and water as one integrated system, the plan shifts from managing constraints to building a complete, resilient, and connected Cooksville.  
			</p>
	<AuthorDate credits={credits} date="PLACEHOLDER DATE"></AuthorDate>
	</div>
	<Footer />

	<Footnotes footnotes={footnotes} />

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
