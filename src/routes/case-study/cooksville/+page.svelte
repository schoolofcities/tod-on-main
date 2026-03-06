<script>

	import '../../../assets/global-styles.css';

	import { onMount, onDestroy } from "svelte";

	import Logo from '$lib/LogoTop.svelte';
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
    import CaseStudyNote from '$lib/CaseStudyNote.svelte';
    import Recommendation from '$lib/Recommendation.svelte';
    import LogoBody from '$lib/LogoBody.svelte';
    import TitlePage from '$lib/TitlePage.svelte';
	const footnoteStore = createFootnoteStore();
	const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		'Canadian Climate Institute, <i>Climate Change and Floods: Fact Sheet</i> (2024), <a href="https://climateinstitute.ca/wp-content/uploads/2024/09/Fact-sheet_-Floods_CanadianClimateInstitute.pdf" target="_blank">URL</a>',
		'Aquafor Beech Ltd., <i>Cooksville Creek Flood Evaluation: Master Plan</i> (2012), <a href="https://www.mississauga.ca/wp-content/uploads/2025/04/23135431/2012-Cooksville-Creek-Flood-Evaluation-Study.pdf" target="_blank">URL</a>',
		'The Center for Transit-Oriented Development, <i>Families and Transit-Oriented Development: Creating Complete Communities for All</i>, TOD 205 (2012), <a href="https://escholarship.org/content/qt618338f0/qt618338f0_noSplash_a6174b2b36ec310cc0b89794f4c8a77f.pdf" target="_blank">URL</a>',
		'Lia Karsten, “Young Families and High-Rise: Towards Inclusive Vertical Family Housing,” <i>Urban Planning</i> 7, no. 4 (2022): 245–52, <a href="https://doi.org/10.17645/up.v7i4.5624" target="_blank">DOI</a>',
		'Karsten, “Young Families and High-Rise."',
		'Fiona Andrews et al., “Best Practice Design and Planning Guidelines for Family-Friendly Apartments,” <i>Urban Policy and Research</i> 41, no. 2 (2023): 164–81, <a href="https://doi.org/10.1080/08111146.2022.2146669" target="_blank">DOI</a>',
		'City of Mississauga, “Mississauga Taking Bold Action to Make Homes More Affordable,” News Release, January 29, 2025, <a href="https://www.mississauga.ca/city-of-mississauga-news/news/mississauga-taking-bold-action-to-make-homes-more-affordable/" target="_blank">URL</a>',
		'Andrews et al., “Best Practice Design and Planning Guidelines for Family-Friendly Apartments.” ',
		'Richard Tucker et al., “Architects’ Professional Perspectives on Child- and Family-Friendly Apartment Design in Australia,” <i>Journal of Asian Architecture and Building Engineering</i> 21, no. 6 (2022): 2262–76, <a href="https://doi.org/10.1080/13467581.2021.1972813" target="_blank">DOI</a>',
		'Fraser Institute, <i>Canada’s Housing Mismatch: Many Canadians Prefer Ground-Oriented Homes, but Not Enough Are Being Built</i> (2023), <a href="https://www.fraserinstitute.org/sites/default/files/canadas-housing-mismatch.pdf" target="_blank">URL</a>',
		'George Baird et al., “The Influence of Demographic and Locational Factors on Occupants’ Perception Scores for Their Buildings,” paper presented at Engaging Architectural Science: Meeting the Challenges of Higher Density: 52nd International Conference of the Architectural Science Association 2018, Melbourne, Australia, December 10, 2018',
		'City of Vancouver, <i>Guidelines: High Density Housing for Families with Children</i> (1992), <a href="https://guidelines.vancouver.ca/guidelines-high-density-housing-for-families-with-children.pdf" target="_blank">URL</a>; City of Toronto, <i>Growing Up: Planning for Children in New Vertical Communities</i>, Urban Design Guidelines (2020),  <a href="https://www.toronto.ca/legdocs/mmis/2020/ph/bgrd/backgroundfile-148362.pdf" target="_blank">URL</a>',
		'Carolyn Whitzman, “Creating Child-Friendly Living Environments in Central Cities: Vertical Living Kids,” in Risk, Protection, <i>Provision and Policy</i>, ed. Tracey Skelton, vol. 12, ed. Claire Freeman and Paul Tranter, Geographies of Children and Young People (Springer Reference, 2017), <a href="https://doi.org/10.1007/978-981-287-035-3_6" target="_blank">URL</a>; Andrews et al., “Best Practice Design and Planning Guidelines for Family-Friendly Apartments.”',
		'Carolyn Whitzman and Dana Mizrachi, “Creating Child-Friendly High-Rise Environments: Beyond Wastelands and Glasshouses,” <i>Urban Policy and Research</i> 30, no. 3 (2012): 233–49, <a href="https://doi.org/10.1080/08111146.2012.663729" target="_blank">DOI</a>',
		'Insurance Bureau of Canada, “July Flash Floods in Toronto and Southern Ontario Caused over $940 Million in Insured Damage,” October 9, 2024, <a href="https://www.ibc.ca/news-insights/news/july-flash-floods-in-toronto-and-southern-ontario-caused-over-940-million-in-insured-damage" target="_blank">URL</a>',
		'Konstantinos M. Andreadis et al., “Urbanizing the Floodplain: Global Changes of Imperviousness in Flood-Prone Areas,” <i>Environmental Research Letters</i> 17, no. 10 (2022): <a href="https://doi.org/10.1088/1748-9326/ac9197" target="_blank">DOI</a>',
		'Andreadis et al., “Urbanizing the Floodplain.”',
		'Catherine Seavitt Nordenson et al., “Reimagining the Floodplain,” in <i>Structures of Coastal Resilience</i>, ed. Catherine Seavitt Nordenson et al. (Island Press/Center for Resource Economics, 2018), <a href="https://doi.org/10.5822/978-1-61091-859-6_3" target="_blank">URL</a>',
		'Seavitt Nordenson et al., “Reimagining the Floodplain.”',
		'Zachary Faza, “Hydro-Urbanism: A Walkable, Coastal Neighborhood Designed to Withstand Flooding and Use Water as a Design Asset” (M.Arch., Florida Agricultural and Mechanical University, 2023), <a href="https://www.proquest.com/docview/2823838389/abstract/ECA1B2705837408APQ/1" target="_blank">URL</a>, p. 6-7',
		'Crystal Aiken et al., <i>Designing With Water: Creative Solutions from Around the Globe</i>, Preparing for the Rising Tide 2 (2014), <a href="https://www.bostonharbornow.org/wp-content/uploads/2017/02/PRT2-Designing-with-Water_Full.pdf" target="_blank">URL</a>, p. 33',
		'Sustainable Business Network of Greater Philadelphia, <i>The Economic Impact of Green City, Clean Waters: The First Five Years</i> (2016), <a href="https://www.sbnphiladelphia.org/wp-content/uploads/2019/09/SBN_FINAL-REPORT.pdf" target="_blank">URL</a>',
		'City of Mississauga, “Mississauga’s Stormwater Infrastructure Helps against a 100-Year Storm,” City of Mississauga, July 23, 2024, <a href="https://www.mississauga.ca/city-of-mississauga-news/news/mississaugas-stormwater-infrastructure-helps-against-a-100-year-storm/" target="_blank">URL</a>',
		'Zachary Faza, “Hydro-Urbanism,” 24-26; American Society of Landscape Architects, “Residential Bioswales and Bioretention Ponds: Improving Water Management,” accessed February 23, 2026, <a href="City of Mississauga, “Mississauga’s Stormwater Infrastructure Helps against a 100-Year Storm,” City of Mississauga, July 23, 2024, " target="_blank">URL</a>',
		'Canadian Infrastructure Council, <i>Building Foundations for Tomorrow: Assessing Housing-Enabling Infrastructure Across Canada</i>, National Infrastructure Assessment Report 1 (2025), <a href="https://canadianinfrastructurecouncil.ca/national-infrastructure-assessment.html" target="_blank">URL</a>',
		'David Thompson, <i>Suburban Sprawl: Exposing Hidden Costs, Identifying Innovations</i> (Smart Prosperity Institute, 2013), <a href="https://institute.smartprosperity.ca/sites/default/files/sp_suburbansprawl_oct2013_opt.pdf" target="_blank">URL</a>',
		'Bernard Deschamps et al., “Flooding: Contributing Factors to Residential Flood Damage in Canada,” <i>International Journal of Disaster Risk Reduction</i> 120 (April 2025): <a href="https://doi.org/10.1016/j.ijdrr.2025.105348" target="_blank">DOI</a>',
		'Costas Armenakis et al., “Flood Risk Assessment in Urban Areas Based on Spatial Analytics and Social Factors,” <i>Geosciences</i> 7, no. 4 (2017), <a href="https://doi.org/10.3390/geosciences7040123" target="_blank">DOI</a>'
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

	<Password correctPassword="meowmeowcat"></Password>

	<!-- Full page title example -->
	<div class="wrapper">
		<!-- Top stays visually on top -->
		<div class="top" style="opacity: {topOpacity}; pointer-events: {topPointer};">
			<TitlePage
				title="Cooksville Station"
				type="Case Study"
				location="Mississauga, ON"
				subtitle="How can we build complete, family-friendly communities while managing flood risk? "
				bgType="Image"
				url={topImage}
				imageOpacity=1
				imageAltText="A photo"
				tintColour="black"
				tintOpacity=0.5
				titleFontColour="var(--brandWhite)"
				subtitleFontColour="var(--brandWhite)"
				secondLogo="II"
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
				backgroundColour={"#F9F9F9"}
				arrowColour={arrowColour}
				on:colourChange={(e) => arrowColour = e.detail}
			/>
		</div>

	</div>


	<div class="text">

		<p>
			Densification near transit means managing the growing risk of flooding while creating communities for everyone. Our Cooksville case explores strategies for more inclusive densification while designing around urban floods.  
		</p>
		
			<CaseStudyNote/>

			<h2 id="Menu_2">
				Neighbourhood overview 
			</h2>
			<p>
				The Cooksville station area is dense, vibrant and diverse. It houses nearly 20,000 residents, nearly 73% of whom are visible minorities. A gateway for immigrants, two-thirds of Cooksville’s residents are foreign-born, and 20% immigrated within the last five years.  
			</p>
		</div>

		<GraphicSingle
			svg720={"../web-assets/case-study/cooksville/Cooksville-720map.svg"}
			svg360={"../web-assets/case-study/cooksville/Cooksville-360map.svg"}
		/>
		
		<div class="text">
			<p>
				The area has many types of households, including families and a growing number of seniors, of whom many live alone. Many people – especially renters – live in high-rise apartments along the major corridors of Hurontario and Dundas streets, but there are also lower-density neighbourhoods further from the station. Household incomes average about $92,000 per year, far below the city average.  
			</p>


		</div>

		<GraphicMultiples
			svgPaths={[
				"../web-assets/case-study/cooksville/cooksville-population.svg",
				"../web-assets/case-study/cooksville/cooksville-age.svg",
				"../web-assets/case-study/cooksville/cooksville-income.svg",
				"../web-assets/case-study/cooksville/cooksville-housing.svg"
			]}
		/>

		<div class="text">

			<div class="caption-container" style="margin-top: 0px; margin-bottom: 60px;">
				<p>
					<span class="caption-source">Data sources: Statistics Canada, Environics Analytics (2024).</span>
				</p>
			</div>

			<p>
				Seeing Cooksville as a high-potential node for growth, the City of Mississauga has set an ambitious future density target of 300 people and jobs per hectare for the station area, roughly triple what is there now. Planning for inclusive growth here will require prioritizing the needs of current and future residents, particularly families. Many elements of successful complete communities are present, mainly centred on the intersection of Hurontario and Dundas – schools, health care, and retail – but access to child care is limited, and the area has a critical gap in community centres. 
			</p>

			<p>
				There is also little existing green space. With few formal civic amenities, residents rely on commercial plazas and small parks for daily needs. And like many suburban areas, the neighbourhood itself is built for the car: wide arterials and fragmented sidewalks make walking and cycling a challenge.  
			</p>

		</div>

		<GraphicSingle
			svg1080={"../web-assets/case-study/cooksville/cooksville-flood-map-1080.svg"}
			svg720={"../web-assets/case-study/cooksville/cooksville-flood-map-720.svg"}
			svg360={"../web-assets/case-study/cooksville/cooksville-flood-map-360.svg"}
		/>

		<div class="text">
			
			<p>
				Another challenge comes from the site itself. The Cooksville station area sits within the Cooksville Creek watershed, which is at risk of flooding in the event of significant storms. The City of Mississauga has undertaken significant stormwater management work in the area, including creating an upstream water storage pond, but high levels of development make this area – like many urban areas on floodplains – vulnerable to inundation.<Footnote id={addFootnote(fns[1])}/> 
			</p>

		</div>

		<ImageSingle
			imageURL={"../web-assets/case-study/cooksville/cooksville-creek-mississauga-photo.jpg"}
			source={"<a href='https://www.mississauga.ca/projects-and-strategies/environmental-assessments/cooksville-creek-erosion-control-from-mississauga-valley-boulevard-to-the-cp-railway/' target='_blank'>Cooksville Creek Erosion Control from Mississauga Valley Boulevard to the CP Railway</a>."}
			caption={"Cooksville Creek experiencing significant bank erosion, highlighting the need for rehabilitation."}
			maxWidth="1080px"
			link='No'
		/>

		<div class="text">
			<p>
				Creating a vibrant community here will require creative approaches to managing risk while increasing access to critical amenities.  
			</p>
	
			<h1 id="Menu_3">
				Cooksville’s current trajectory 
			</h1>

			<p>
				A recent surge in investment and proposed development in the area as the Hazel McCallion line nears completion suggests developer confidence in Cooksville’s potential. Dozens of high-rise projects are in the pipeline, set to transform surface parking lots and aging retail plazas into mixed-use towers. 
			</p>

			<p>
				If growth continues this way, it will be concentrated on a handful of underused commercial and industrial lots. The default is towers on steel or concrete podiums – a built form that can increase density and incorporate ground-floor mixed uses while efficiently building upper floors. New towers are clustered on lots in a fragmented pattern, with density through height to offset costly flood mitigation measures in basements and ground floors. 
			</p>

		</div>

		<ImageSingle
			imageURL="../web-assets/case-study/cooksville/cooksville-current-dev.png"
			caption="Currently proposed or under construction development 800m from Cooksville station."
			source="Photo by Infrastructure Institute (2025)."
			maxWidth="680px"
			link='No'
		/>

		<div class="text">	

			<p>
				But this does not necessarily create a livable neighbourhood, and without early investment in civic infrastructure, Cooksville risks becoming just a collection of towers: dense but socially thin. Crucial infrastructure is not keeping pace. The Cooksville Community Hub, co-located with the Thomas L. Kennedy Secondary School, is planned but needs funding. Other cultural amenities are largely non-existent.  Local parks are small and discontinuous, and few institutional sites exist to anchor future population growth.  
			</p>

		</div>

		<ImageSingle
			imageURL="../web-assets/case-study/cooksville/cooksville-community-hub.jpg"
			caption="Rendering of the planned Cooksville Community Hub, illustrating a vibrant community space."
			source="<a href='https://www7.mississauga.ca/documents/committees/pdc/2016/06_27_16_-_PDC_Agenda_-_Evening_Session.pdf' target='_blank'>Photo by the City of Mississauga</a>."
			maxWidth="680px"
			link='No'
		/>
		
		<div class="text">

			<p>
				Building a more complete community here requires more intentional planning – for families, and for floods. Here’s how it could be done. 
			</p>

		</div>

		<ImageCompare
			imageURL1="../web-assets/case-study/cooksville/cooksville-scenario1.png"
			caption1=""
			source1=""
			buttonLabel1="Current trajectory"
			imageURL2="../web-assets/case-study/cooksville/cooksville-scenario2.png"
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

			<h1 id="Menu_4">
				Optimized scenario: Building for families, building for all 
			</h1>

			<p>
				Many families want to live near transit because they can spend less time and money on driving and benefit from better access to education and culture in well-planned developments.<Footnote id={addFootnote(fns[2])}/> Yet even though families have always lived in these kinds of spaces, new mid- and high-rise construction is often oriented toward individuals or couples without children.<Footnote id={addFootnote(fns[3])}/> Our first set of recommendations for improving on Cooksville’s current trajectory explores ways to include different kinds of families in TOD. Improving the number and kind of family-oriented units, with targeted community upgrades, can increase density around transit and benefit all residents. 
			</p>
			
			<Recommendation style=1 count=1
				title="Provide more 2- and 3- bedroom units"/>

			<p>
				The best way to include families in growth is to give them the space they need. Cramped spaces and an insufficient number of bedrooms are the most common concerns cited by both children and adults in high-rise dwellings.<Footnote id={addFootnote(fns[4])}/> In Mississauga, two-thirds of households are families, but most proposed new buildings allocate 70% of units as studios or 1-bedrooms. Units with two or more bedrooms allow more flexible space for families and multi-generational households.<Footnote id={addFootnote(fns[5])}/> 
			</p>
		</div>

		<GraphicSingle
			svg720={"../web-assets/case-study/cooksville/cooksville-scenario-comparison-720.svg"}
			svg360={"../web-assets/case-study/cooksville/cooksville-scenario-comparison-360.svg"}
		/>

		<div class="text">

			<p>
				Our research has shown that this way of building also lowers emissions because there are generally fewer kitchens and bathrooms in larger units, where they are shared by several people in the unit. This kind of floor plan also increases density within buildings and allows for a reduction in height. With shorter towers, more mid-rise buildings can be introduced to create active, human-scaled street fronts.  
			</p>

			<p>
				Mississauga has already taken steps to incentivize this kind of unit mix by eliminating municipal development charges for units with 3 or more bedrooms in purpose-built rental apartments.<Footnote id={addFootnote(fns[6])}/> This incentive could be expanded by similarly eliminating these charges at the regional level, or for all new buildings. Other countries, such as Ireland, go further and prescribe a mix of apartment sizes and bedroom numbers before new developments are approved.<Footnote id={addFootnote(fns[7])}/>
			</p>

			<Recommendation style=1 count=2
							title="Adopt Canadian and global benchmarks for family-friendly living at the site level"/>
			<p>
				In addition to the number of bedrooms, spaces within units must be flexible. Some cities, including Toronto in its <i>Growing Up</i> guidelines for vertical communities, suggest having a recommended play space of 2 by 3 metres within units. Guidelines such as these make planning for larger households more concrete. 
			</p>

			<p>
				Safety and connection are also essential, with many studies citing windows and balconies as areas that can be improved with required safety mechanisms to make units more family- friendly.<Footnote id={addFootnote(fns[8])}/> Within buildings, ensuring that there are shared spaces, courtyards with play areas, and facilities that children can access – including elevator buttons at child level – encourages connection and independence. 
			</p>

			<p>
				Easy interaction with the street can mitigate a lack of private outdoor space, making density more appealing. Many families have expressed a preference for “ground-oriented housing,” which is housing with direct access to a street or public space that doesn’t pass through a shared corridor or elevator, and which is often found with missing middle-type housing.<Footnote id={addFootnote(fns[9])}/>
			</p>

			<p>
				In their design guidelines, cities can also ensure buildings are surrounded by green spaces with places to play – not just planted gardens or inaccessible hardscape – away from busy roads.<Footnote id={addFootnote(fns[10])}/> 
			</p>

		</div>

		<ImageSingle 
			imageURL="../web-assets/case-study/cooksville/copenhagen-playground.jpg" 
			maxWidth="680px"
			caption={"Playground and green space designed for safe, accessible play"}
			source={"<a href='https://www.pexels.com/photo/modern-playground-in-copenhagen-urban-area-34770471/' target='_blank'>Photo by Hari Hofer</a>"}
		/>

		<div class="text">

			<Recommendation style=1 count=3
							title="Prioritize family-friendly retail and amenities in the surrounding area "/>
			<p>
				At the neighbourhood level, Canadian cities have long been leaders in setting guidelines for what services should be available nearby, from schools to transit stops to grocery stores.<Footnote id={addFootnote(fns[11])}/> Our optimized plan for Cooksville Station builds on this, integrating community theatres, youth centres, and libraries directly into new mixed-use blocks.  
			</p>

			<p>
				Like many people, families enjoy the benefits of compact urban living: proximity to jobs and schools, a diversity of people and stores, and recreational amenities like swimming pools.<Footnote id={addFootnote(fns[12])}/> Ensuring that child care and school amenities keep pace with density is a core element of growth. A mix of retail is important for all communities, but inexpensive shops are particularly important for young people. In focus groups, children have also specifically identified outdoor spaces to play and libraries as preferred local amenities, and these places are disproportionately used by children.<Footnote id={addFootnote(fns[13])}/> 
			</p>

		</div>

		<ImageSingle imageURL="../web-assets/case-study/cooksville/mixed-use-space.png"
			caption="Mixed use public space, designed for all ages."
			maxWidth="680px"
			source="Photo by Infrastructure Institute (2025)."
		/>

		<div class="text">

			<h1 id="Menu_5">
				Addressing rising flood risk 
			</h1>

			<p>
				The past 20 years have seen significant urban floods across Canada, including in Calgary, Winnipeg, Toronto – and Mississauga. In 2024, a 100-year storm caused $940 million in flood damage across the region.<Footnote id={addFootnote(fns[14])}/> Since 1985, Southern Ontario has experienced rapid urbanization in areas of increasing flood exposure.<Footnote id={addFootnote(fns[15])}/> As in many Canadian neighbourhoods, future growth in Cooksville will need to balance density with minimizing risk and flood exposure. Our second set of recommendations addresses this growing need. 
			</p>

			<Recommendation style=1 count=1
							title="Minimize impermeable surfaces and costly engineering through parcel selection"/>

			<p>
				The “tall and sprawl” model of urban growth – which features high-rise towers surrounded by lower-density, often single-family, homes – is often criticized, but in flood zones it can make sense. Many properties east of Hurontario Street are regulated by the Credit Valley Conservation Authority, meaning that any development in this area must undergo strict flood mitigation to proceed. These guidelines incentivize taller growth on smaller footprints. In part, this is because urbanization increases the area of impermeable surfaces, such as parking lots, roads, and buildings, where water cannot soak into the ground.<Footnote id={addFootnote(fns[16])}/> Choosing sites that limit additional impermeable surface area decreases this risk. 
			</p>

			<p>
				Our optimized approach starts by adopting the current city strategy for <i>where</i> to build: on underused parcels, like aging plazas and surface parking lots. Accounting for floodplain considerations and preserving existing neighbourhoods, these are the parcels most eligible for development. This leaves stable residential neighbourhoods mostly untouched.  
			</p>

		</div>

		<!-- <ImageSingle imageURL="../web-assets/case-study/cooksville/palmerston.jpg"
			caption="Example of a green buffer on Palmerston Ave., Toronto"
			maxWidth="680px"
			source="Photo by Jeff Allen (2025)."
		/> -->

		<div class="text">

			<Recommendation style=1 count=2
							title="Invest in multi-benefit green infrastructure"/>

			<p>
				Today, developers are engineering their way around the floodplain with elevated podiums, underground storage tanks, and on-site water detention systems. These “grey infrastructure” strategies are expensive and, buried below grade, invisible to the public eye.  
			</p>

			<p>
				But what if we approached floodplain mitigation as an opportunity to improve public space? This moves beyond simply burying water tanks underground to lower flood risk, building instead natural, “green” infrastructure such as parks, pathways, and design features.<Footnote id={addFootnote(fns[17])}/> For example, bioswales – sloping basins of soil and plants next to paved areas – can capture and clean rainwater runoff while providing attractive greenery. Rain gardens and green roofs provide similar benefits and divert water from overloaded storm drains. 
			</p>

			<p>
				By weaving this green infrastructure across sites, we can create daily spaces for social connection: new pathways, parks, and adaptive landscapes that guide future development. The more developers who adopt this strategy, the larger the green space network, amplifying benefits for the entire community. 
			</p>

			<p>
				Multi-benefit infrastructure like this can be more expensive upfront because it often features layered built and landscape improvements, and therefore involves the time and expertise of many people (such as engineers, ecologists, and architects).<Footnote id={addFootnote(fns[18])}/> 
			</p>

			<p>
				But it can increase the appeal of the area, and neighbouring property values.<Footnote id={addFootnote(fns[19])}/> 
			</p>

			<p>
				Cheonggyecheon Urban Park in South Korea combines public space with flood mitigation when needed, and has contributed significantly to the 30-50% increase in neighbouring land value.<Footnote id={addFootnote(fns[20])}/> Green stormwater improvements in Philadelphia have increased nearby home values by 10%, which also contributes to the city’s tax base.<Footnote id={addFootnote(fns[21])}/> 
			</p>

		</div>

		<ImageSingle
			imageURL={"../web-assets/case-study/cooksville/seoul-river.jpg"}
			caption="When Cheonggeyechon River is low, pedestrians can enjoy walking through the flood infrastructure in-between busier main streets."
			source="<a href='https://commons.wikimedia.org/wiki/File:Cheonggeyechon_River_in_Seoul.jpg' target='_blank'>Photo by Ken Eckert</a>"
			maxWidth="680px"
			link='No'
		/>

		<ImageSingle
			imageURL={"../web-assets/case-study/cooksville/cheonggyecheon.jpg"}
			caption="When Cheonggeyechon River is low, pedestrians can enjoy walking through the flood infrastructure in-between busier main streets."
			source="<a href='https://commons.wikimedia.org/wiki/File:20240602_175752_Cheonggyecheon_06.jpg' target='_blank'>Photo by Dwxn</a>"
			maxWidth="680px"
			link='No'
		/>

		<div class="text">

			<Recommendation style=1 count=3
							title="Maintain and improve current stormwater infrastructure, while prioritizing infill over sprawl "/>

			<p>
				Continued investment in stormwater infrastructure by all orders of government will be critical for Cooksville. Previous municipal efforts – including an upstream stormwater pond – helped to protect the neighbourhood from severe flooding in 2024, and the City has approved a $308-million stormwater management plan for the next decade.<Footnote id={addFootnote(fns[22])}/> City-wide, more features like this, as well as more soil and vegetation that can absorb and filter water, will decrease the risk of overwhelming aging infrastructure, with the added benefit of decreasing contamination from fertilizers, pesticides, and vehicles that runs off into drains.<Footnote id={addFootnote(fns[23])}/> 
			</p>

			<p>
				Continuing to build in dense TODs instead of in patterns of sprawl will slow new infrastructure build-out, and the costs associated with maintaining thousands of kilometres of roads and pipes.<Footnote id={addFootnote(fns[24])}/> Where Canadian cities have calculated the cost of spawl, they have found that more compact development patterns typically range from 30-70% less expensive than greenfield development, translating to capital and operating budget savings in the hundreds of millions per year.<Footnote id={addFootnote(fns[25])}/> 
			</p>
			
		</div>

		<ImageSingle
			imageURL={"../web-assets/case-study/cooksville/saigon-park.jpg"}
			caption="Lake Saigon stormwater management pond."
			source="<a href='https://www.mississauga.ca/wp-content/uploads/2024/08/19124804/Siagon-Park-Social-Post-1-scaled.jpg' target='_blank'>Photo by the City of Mississauga.</a>"
			maxWidth="680px"
			link='No'
		/>

		<div class="text">

			<Recommendation style=1 count=4
							title="Develop more comprehensive understanding of flood risk in TOD areas"/>

			<p>
				It is not just proximity to water that carries a flood risk, but how vulnerable people and assets are to exposure.<Footnote id={addFootnote(fns[26])}/> Cooksville is considered a high-risk area in part because of social factors, including large populations of seniors and young children, high numbers of renters, lower incomes, and language barriers.<Footnote id={addFootnote(fns[27])}/> The area also has more older building stock (built before 1980) than many neighbourhoods in Mississauga. These homes can have weaker foundations and less flood protection than newer construction. 
			</p>

		</div>

		<ImageSingle
			imageURL={"../web-assets/case-study/cooksville/cooksville-aerial.jpg"}
			caption="Aerial view of Cooksville showing family homes."
			source="<a href='https://commons.wikimedia.org/wiki/File:Aerial_view_of_Cooksville_2022.jpg' target='_blank'>Photo by Canmenwalker.</a>"
			maxWidth="680px"
			link='No'
		/>

		<div class="text">

			<p>
				In Cooksville, as in many neighbourhoods across the country, developing a comprehensive understanding of how built form and social vulnerability interact with flood risk geography can shape planning interventions such as building code changes, targeted incentives to repair, or zoning that incentivizes more concentrated development. 
			</p>

			<p>
				Green and social infrastructure can come together here in a win-win for the community, with vibrant local shops and public facilities woven into a landscape where green corridors double as flood protection and public parks. By treating housing, amenities, and water as one integrated system, the plan shifts from managing constraints to building a complete, resilient, and connected Cooksville.  
			</p>
			

		</div>

			<ImageSingle imageURL="../web-assets/case-study/cooksville/green-infrastructure.png"
				caption="Green infrastructure with art gallery in the back."
				maxWidth="680px"
				source="Photo by Infrastructure Institute (2025)."
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
