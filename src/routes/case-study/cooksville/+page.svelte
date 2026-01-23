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

	import topImage from './assets/CC_Background_Frame_1.png' 

	export let data;

	// const scrollyContentSmall = [
	// 	{
	// 		image: "./examples/amroth-iso-lot.png",
	// 		text: "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>"
	// 	},
	// 	{
	// 		image: "./examples/amroth-iso-bldg.png",
	// 		text: "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>"
	// 	},
	// 	{
	// 		image: "./examples/wilson-iso-lot.svg",
	// 		text:"<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>"
	// 	},
	// 	{
	// 		image: "./examples/wilson-iso-bldg.svg",
	// 		text: "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>"
	// 	},
	// ];
	
	import Footnote from '$lib/Footnote.svelte';
	import Footnotes from '$lib/Footnotes.svelte';
	import { createFootnoteStore } from '$lib/footnoteUtils';
    import { resolveRoute } from '$app/paths';
    import HamburgerMenu from '$lib/HamburgerMenu.svelte';

	const footnoteStore = createFootnoteStore();
	const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		'Hello I am a footnote',
		'Hello I am a second <a href="https://example.com" target="_blank">footnote</a> with a link',
		'Author (Year) Publication information etc this might be a citation or a reference to a source',
		'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla.'
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


	<div id="text_1" class="text">
		

			<h1>Why this matters </h1>
			<p>
				Adding density around transit stations requires planning for different kinds of households. Over 35% of Canadian households contain three or more people, but much of the existing and planned housing near transit stations is designed for individuals or couples.1 
			</p>
			<p>	
				Cities are also facing greater risks from a changing climate, with flooding the most frequent and costly impact across the country.2 This case explores strategies for more inclusive densification while managing flood risk. 
			</p>
			<h2>
				Neighbourhood overview 
			</h2>
			<!-- <p>
				Mississauga’s Cooksville neighbourhood is a future transit hub where the existing GO rail line will converge with the new Hazel McCallion light rail transit (LRT) and Dundas Bus Rapid Transit (BRT) lines, making it a focal point for growth.
			</p> -->
			<p>
				With over 30,000 residents, Cooksville is dense, vibrant and diverse. Nearly 73% are visible minorities. A gateway for immigrants, two-thirds of Cooksville’s residents are foreign-born, and one in five is a recent arrival.  
			</p>
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
			<p>
				There is also little existing green space. With few formal civic amenities, residents rely on commercial plazas and small parks for daily needs. And like many suburban areas, the neighbourhood itself is built for the car: wide arterials and fragmented sidewalks make walking and cycling a challenge.  
			</p>
			<p>
				Another challenge comes from the site itself. Cooksville has over 300 buildings sitting on the Cooksville Creek floodplain, and the area has been deemed a flood risk. 
			</p>

			<!-- MAP OF FLOOD PLAIN -->

			<p>
				Creating a thriving community here will require creative approaches to managing risk while increasing access to critical amenities.  
			</p>


			<h1>
				Cooksville’s current trajectory 
			</h1>

			<p>
				A recent surge in investment and proposed development in the area as the Hazel McCallion line nears completion suggests developer confidence in Cooksville’s potential.3 Dozens of high-rise projects are in the pipeline, set to transform surface parking lots and aging retail plazas into mixed-use towers. 
			</p>

		</div>

		<ImageCompare
			imageURL1="../web-assets/case-study/cooksville/cooksville-current-built.png"
			caption1=""
			source1="Infrasturcture Institute, School of Cities"
			buttonLabel1="Current and future rapid transit"
			imageURL2="../web-assets/case-study/cooksville/cooksville-current-dev.png"
			caption2=""
			source2="Infrasturcture Institute, School of Cities"
			buttonLabel2="Planned development"
			maxWidth="680px"
			link='No'
		/>

		<div class="text">	

			<p>
				If growth continues this way, it will be concentrated on a handful of underused commercial and industrial lots. The default is towers on podiums – a built form tried and tested for effectively increasing density. 
			</p>

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
			source1="Infrasturcture Institute, School of Cities"
			buttonLabel1="Current trajectory"
			imageURL2="../web-assets/case-study/cooksville/cooksville-scenario2.png"
			caption2=""
			source2="Infrasturcture Institute, School of Cities"
			buttonLabel2="Mixed-use scenario"
			maxWidth="680px"
			link='No'
		/>

		<div class="text">	

			<h1>
				Building for families, building for all 
			</h1>

			<p>
				New mid- and high-rise construction is often oriented toward individuals or couples without children, even though families have always lived in these kinds of spaces.4 Improving the number and kind of family-oriented units, with targeted community improvements, can increase density around transit and benefit all residents. 
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

			<h1>
				Addressing rising flood risk 
			</h1>

			<p>
				The past 20 years have seen significant urban floods across Canada, including in Calgary, Winnipeg, Toronto -- and Mississauga, including one in 2024 that caused $$ of damage across the city.14 Southern Ontario in particular has been a site of increasing urbanization in areas of increasing flood exposure since 1985.15 As in many Canadian neighbourhoods, future growth in Cooksville will need to balance density with minimizing risk and flood exposure.  
			</p>

			<h3>
				Recommendation 1: Minimize impermeable surfaces and costly engineering through parcel selection 
			</h3>

			<p>etc etc</p>

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
