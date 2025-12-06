<script>

	import '../../../assets/global-styles.css';

	import { onMount, onDestroy } from "svelte";

	import Logo from '$lib/LogoTop.svelte';
	import TitleFullPage from '$lib/TitleFullPageCaseStudy.svelte';
	import TitleHalfSplit from '$lib/TitleHalfSplit.svelte';
	import TitleStandard from '$lib/TitleStandard.svelte';
	import AuthorDate from '$lib/AuthorDate.svelte';
	import ImageSingle from '$lib/ImageSingle.svelte';
	import GraphicSingle from '$lib/GraphicSingle.svelte';
	import GraphicsMultiples from '$lib/GraphicMultiples.svelte';
	import Footer from '$lib/Footer.svelte';

	import topImage from './assets/CC_Background_Frame_1.png' // TODO: MAKE THIS DARK
	import featureImage from './assets/cooksville-transit-schematic.png'

	import FadingImages from "$lib/FadingImages.svelte";
	const scrollyContentBig = [
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_2.png",
			text: [""],
			arrowColour: "white"
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_2.png",
			text: [""],
			arrowColour: "white"
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_3.png",
			text: [""]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_4.png",
			text: ["<p>Cooksville Station, Mississauga. A future transit super-hub where the GO train will meet the new Hazel McCallion LRT and Dundas Bus Rapid Transit (BRT) will converge, making it a focal point for massive growth.</p><p>Matching it is a lofty density target of 300 people and jobs per hectare.</p>", 
					"<p>However, limitations abound. At its periphery are long-standing neighbourhoods. It is also one of the most physically constrained parts of the city. Termed a “Flood Risk MTSA”, it has over 300 buildings sitting within the Cooksville Creek floodplain.</p><p>Creating a complete community here means balancing complex technical, social, and regulatory hurdles within a limited footprint.</p>"
					]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_5.png",
			text: ["<p>So, who lives here now?</p><p>Cooksville is Mississauga's quintessential gateway. A vibrant, first-stop neighbourhood for nearly 20,000 people, where 1 in 5 residents is a recent arrival.</p>"]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_6.png",
			text: ["<p>It's also a community of renters: over half of all residents rent (50.7%), with most living in high-rise apartments (68.1%).</p><p>Two-thirds of households are families, alongside a growing number of seniors of whom many live alone. </p>"]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_7.png",
			text: ["<p>Public life is centered at the \"Four Corners\" of Hurontario and Dundas.</p><p>With few formal civic amenities, residents rely on commercial plazas and small parks for daily needs.</p><p>Beyond this intersection, amenities quickly thin out, creating a gap between density and daily life.</p>",
					"<p>It is also a socio-economically poorer area.</p><p>Household incomes average about $92,000 per year, starkly lower than the city's average.</p>"
					]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_8.png",
			text: ["<p>And residents here rely on public transit – more than 57% of the Mississauga average. </p><p>Yet the neighbourhood itself is built for the car. Wide arterials and fragmented sidewalks make walking and cycling a challenge.</p>"]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_9.png",
			text: ["<p>Adding to the challenge is the land itself.</p><p>Many properties east of Hurontario St are Credit Valley Conservation (CVC)-regulated.</p>",
					"<p>Under CVC rules, development in this area must undergo strict flood mitigation to proceed. It also incentivizes taller growth onto smaller footprints.</p>"
					]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_10.png",
			text: ["<p>Despite the limitations, development is booming.</p><p>Dozens of high-rise projects are in the pipeline, set to transform surface parking lots and aging retail plazas into mixed-use towers.</p>"]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_11.png",
			text: ["<p>Developers are engineering their way around the floodplain: elevated podiums, underground storage tanks, and on-site detention systems. Expensive, and buried below grade, invisible to the public eye.</p>"]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_12.png",
			text: ["<p>Some civic infrastructure, including the Cooksville Community Hub co-located with the TL Kennedy Secondary School, has been planned.</p><p>A new skyline is coming to fruition, driven by transit investment and the city's growth targets.</p>"]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_13.png",
			text: ["<p>What happens if we continue this way?</p>"]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_14.png",
			text: ["<p>Accounting for floodplain considerations and stable neighbourhoods, these are the parcels most eligible for development. </p><p>Growth becomes concentrated on a handful of underused commercial and industrial lots. </p>",
					"<p>The default is towers on podiums – a built form tried and tested to generate density effectively.</p>",
					"<p>But does this create a livable neighbourhood?</p><p>Crucial infrastructure is not keeping pace. The Cooksville Community Hub, while planned, needs funding. Other cultural amenities are virtually non-existent.</p>",
					"<p>Local parks are small and discontinuous, and few institutional sites exist to anchor future population growth.</p><p>New towers cluster on fragmented lots, with density pushed further up to offset costly flood mitigation measures.</p><p>Without early investment in civic infrastructure, Cooksville risks becoming a collection of towers: dense but socially thin. </p>"
					]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_15.png",
			text: ["<p><strong>Is this really the best we can build?</strong></p>"]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_16.png",
			text: ["<p>The challenge isn't just accommodating density. It's catalyzing it to create connected and amenity-rich communities where residents can flourish.</p>",
				"<p>Here's how we could do it.</p>",
				"<p>Our approach starts by adopting the current strategy for where to build: underused parcels like aging plazas and surface parking lots.</p><p>This leaves stable residential neighbourhoods mostly untouched.</p>"
				]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_17.png",
			text: ["<p>Next, let's reframe the floodplain restriction.</p><p>What happens when we approach floodplain mitigation as a public realm opportunity? This means moving beyond simply burying water tanks underground.</p><p>By weaving (less expensive!) green infrastructure across sites, we create daily spaces for social connection: new pathways, parks, and adaptive landscapes that guide future development.</p>",
				"<p>The more developers who adopt this strategy, the larger the green network, amplifying benefits for the entire community.</p>"
				]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_18.png",
			text: ["<p>Now let's turn our attention to build for the life that's already here.</p><p>Data shows most residents enjoy an engaged urban life, including concerts, restaurants, fitness classes, sports, and galleries. The current landscape doesn't reflect that.</p>",
					"<p>In a growing community, social infrastructure and third places are just as important as housing.</p><p>The optimized plan focuses on creating spaces for gathering - integrating community theatres, youth centres, and libraries directly into new mixed-use blocks.</p>",
					"<p>Finally, let's build housing for how people actually live.</p><p>Two-thirds of households are families, yet the average new proposal allocates around 70% of new units as 1-bedrooms.</p>",
					"<p>The market is sending an undeniable signal too. Demand for 1-bedrooms is low, with supply outpacing demand. Meanwhile, larger units are outperforming them,  with 2.5 times the sales volume – many selling above asking price.</p><p>Building what the community needs is the obvious direction.</p><p>This means prioritizing units with two or more bedrooms for families and multi-generational households.</p>",
					"<p>This is also a more efficient way to build. Larger, family-sized units house more people in a smaller total footprint.</p><p>Think of it this way: 3 people in a 3-bedroom share 1 kitchen. 3 people in 3 separate 1-bedrooms require 3 separate kitchens.</p><p>It allows for a reduction in extreme height. Towers can be shorter, and more mid-rise buildings can be introduced to create active, human-scaled street fronts.</p>"
					]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_16.png",
			text: ["<p>In this vision, density is achieved through a connected urban fabric - a mix of housing forms for how people actually live.</p><p>Social infrastructure, from the community hub to vibrant local shops, is woven into a landscape where green corridors double as flood protection and public parks.</p><p>By treating housing, amenities, and water as one integrated system, the plan shifts from managing constraints to building a complete, resilient, and connected Cooksville.</p>"]
		},
		{
			image: "../web-assets/case-study/cooksville/CC_Background Frame_19.png",
			text: [""]
		},
	];

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
    import BottomArrow from '$lib/BottomArrow.svelte';

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

	onMount(() => {
		innerHeight = window.innerHeight;

		const onScroll = () => {
			scrollY = window.scrollY;
		};

		window.addEventListener('scroll', onScroll, { passive: true });
		return () => window.removeEventListener('scroll', onScroll);
	});

	$: topOpacity = 1 - Math.min(scrollY / innerHeight, 1);

	$: topPointer = topOpacity < 0.02 ? 'none' : 'auto';

	let arrowColour = "white";

</script>



<svelte:head>

	<title>TOD-on-main | School of Cities</title>

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

	<meta name="citation_title" content="Design Components">
	<meta name="citation_author" content="Author Name 1">
	<meta name="citation_author" content="Author Name 2">
	<!-- <meta name="citation_author" content="Author Name 3"> -->
	<meta name="citation_publication_date" content="2025/09/23">
	<meta name="citation_journal_title" content="School of Cities">
	<!-- <meta name="citation_pdf_url" content="https://schoolofcities.utoronto.ca/research-paper.pdf"> -->
	<meta name="citation_abstract_html_url" content="https://schoolofcities.github.io/design-components/">

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
				subtitle="How do you build a high-density community bound by natural and physical land restrictions?"
				image={topImage}
				imageOpacity=1
				imageAltText="A photo"
				imageFeature={featureImage}
				titleFontColour="var(--brandWhite)"
				subtitleFontColour="var(--brandWhite)"
				authorText="Author Name, Author Name, Author Name"
				dateText="~ December, 2025"
				topOpacity={topOpacity}
			/>
		</div>
		
		<BottomArrow 
		clickable={true}
		colour={arrowColour}/>

		<!-- Bottom is underneath, scrolls normally -->
		<div class="bottom">
			<FadingImages
				sections={scrollyContentBig}
				imageAlign={"right"}
				imageWidth={"100%"}
				imageHeight={"100dvh"}
				textSectionMaxWidth={"400px"}
				textSectionAlign={"left"}
				fadeDuration={1500}
				mobileTextAlign={"top"}
				bind:arrowColour
			/>
		</div>

	</div>





	
	

	

	

	


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

	<!-- <Logo logoType="Blue" backgroundColor="var(--brandWhite)"/>

	<ImageSingle
		imageURL="https://jamaps.github.io/photos/picimgs/taipei1_2025.jpg"
		caption="Taipei skyline."
		source="Jeff Allen."
		altText=""
		maxWidth="1080px"
	/>


	<TitleStandard
		title="Fun Captivating Project Title"
		subtitle="Maybe a slightly longer more detailed wordier project subtitle "
	/>

	<div class="text">

		<AuthorDate
			authors="<a href='' target='_blank'>Author Name</a> & <a href='' target='_blank'>Author Name</a>"
			date="July 2025"
		/>

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla. 
		</p>

		<p>
			Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci.<Footnote id={addFootnote(fns[0])}/> nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla.
		</p>

		<p>
			Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed.<Footnote id={addFootnote(fns[1])} />
		</p>

		<p>
			Nunc vel massa turpis. Vivamus id odio ut nulla dignissim molestie. 
		</p>

	</div>

	<GraphicSingle
		svg720="./examples/map-tree-redline-720.svg"
		svg360="./examples/map-tree-redline-360.svg"
	/>
	
	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla.<Footnote id={addFootnote(fns[2])} />
		</p>
		<p>
			Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla.<Footnote id={addFootnote(fns[3])} />
		</p>
		<p>
			Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed.<Footnote id={addFootnote(fns[0])} />
		</p>
		<p>
			Nunc vel massa turpis. Vivamus id odio ut nulla dignissim molestie. 
		</p>

	</div>

	<GraphicsMultiples
		svgPaths={["./examples/map-tree-360.svg", "./examples/map-heat-360.svg", "./examples/map-asthma-360.svg"]}
	/>

	

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla.<Footnote id={addFootnote(fns[2])} />
		</p>
		<p>
			Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla.<Footnote id={addFootnote(fns[3])} />
		</p>
		<p>
			Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed.<Footnote id={addFootnote(fns[0])} />
		</p>
		<p>
			Nunc vel massa turpis. Vivamus id odio ut nulla dignissim molestie. 
		</p>

	</div> -->

	<!-- <ScrollyImages
		sections={scrollyContentSmall}
		imageAlign={"center"}
		imageWidth={"540px"}
		imageHeight={"540px"} 
		textSectionMaxWidth={"540px"}
		textSectionAlign={"right"}
		fadeDuration={500}
	/> -->

	


	
	<div class="text">
		<p>
			Fusce sed sem nulla. Praesent congue sapien pellentesque sodales fermentum. Pellentesque dapibus ultrices lacus consectetur laoreet. Integer imperdiet sed sapien sed pharetra. Praesent sodales nunc ut lorem venenatis laoreet vitae et neque. Etiam condimentum tincidunt dignissim. 
		</p>

		

		<p>	
			Praesent placerat purus vitae rhoncus auctor. Aliquam faucibus porta scelerisque. In bibendum ornare sagittis. Nam accumsan turpis sit amet elementum sollicitudin. Mauris auctor nec velit id iaculis. Proin venenatis nisl a iaculis dignissim. Nunc volutpat nulla at dolor mollis eleifend. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam commodo purus in risus placerat, sed vehicula enim viverra. 
		</p>
		<h2>
			A subheading that is nice
		</h2>
		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla. 
		</p>
		<p>
			Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla. 
		</p>
		<p>
			Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed. 
		</p>
		<h3>
			A subheading that is nice
		</h3>
		<p>
			Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla. 
		</p>
		<p>
			Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed. 
		</p>

	</div>



	<div class="text">

		<div class="details">

			<h2>
				Extra details 
			</h2>
			<p>
				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla. 
			</p>
			<p>
				Cras tincidunt nisi non tempus suscipit. Nullam metus erat, ultrices vitae mauris commodo, placerat sollicitudin sem. In vitae dignissim eros. Phasellus porttitor orci nisl, vitae iaculis nulla pretium et. Fusce nec tortor erat. Vestibulum pretium nisl et ligula ultrices fringilla. 
			</p>
			<p>
				Vivamus non finibus erat. Ut quis mi at felis aliquam rhoncus eu eget augue. Nunc convallis, dui et congue suscipit, nisl sapien malesuada ligula, vitae luctus justo ligula finibus diam. Quisque aliquam et lacus vitae venenatis. Duis id vulputate augue, vel posuere ex. Nam fermentum consequat dolor, ac finibus justo finibus sit amet. Nam suscipit egestas tellus, malesuada dignissim neque dignissim sed. 
			</p>

		</div>

	</div>

	<div class="text">

		<Footnotes footnotes={footnotes} />
		
	</div>

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
		z-index: 2;
		pointer-events: none; /* allows clicks to pass through if needed */
		transition: opacity 0.1s linear;
	}

	.bottom {
		position: relative;
		z-index: 1;
		min-height: 100vh; /* ensures it fills viewport behind top */
	}

	
</style>
