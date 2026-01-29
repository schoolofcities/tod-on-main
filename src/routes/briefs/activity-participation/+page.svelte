<script>

	import '../../../assets/global-styles.css';

	import Logo from '$lib/LogoBody.svelte';
	import TitleFullPage from '$lib/TitleFullPageCaseStudy.svelte';
	import TitleHalfSplit from '$lib/TitleHalfSplit.svelte';
	import TitleStandard from '$lib/TitleStandard.svelte';
	import AuthorDate from '$lib/AuthorDate.svelte';
	import ImageSingle from '$lib/ImageSingle.svelte';
	import GraphicSingle from '$lib/GraphicSingle.svelte';
	import GraphicsMultiples from '$lib/GraphicMultiples.svelte';
	import Footer from '$lib/Footer.svelte';
	import ScrollyImages from "$lib/ScrollyImages.svelte";
	import LineBreakMiniTransitMap from '$lib/LineBreakMiniTransitMap.svelte';

	import imageBus from "./assets/ttc-bus-1080.jpg";
	
	import Footnote from '$lib/Footnote.svelte';
	import Footnotes from '$lib/Footnotes.svelte';
	import { createFootnoteStore } from '$lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
	const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		'Hello I am a footnote',
		'Hello I am a second <a href="https://example.com" target="_blank">footnote</a> with a link',
		'Author (Year) Publication information etc this might be a citation or a reference to a source',
		'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consequat lacus eu dolor dapibus sodales. Aenean venenatis metus id eleifend tincidunt. Nulla ut lacus et urna finibus bibendum sit amet et ante. Aliquam tristique, ex sed porttitor hendrerit, ex odio accumsan ex, eu maximus leo quam quis nulla.'
	];

</script>



<svelte:head>

	<title>Activity participation | School of Cities</title>

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

	<!-- Full page title example -->

	<!-- <TitleFullPage
		title="Fun Captivating Project Title"
		subtitle="Maybe a slightly longer more detailed wordier project subtitle"
		image="https://jamaps.github.io/photos/picimgs/halifax2_2024.jpg"
		imageOpacity=0.9
		imageAltText="A photo"
		titleFontColour="var(--brandWhite)"
		subtitleFontColour="var(--brandWhite)"
		logoType="White"
	/> -->


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

	<div class="text" style="margin-top: 150px; margin-bottom: 20px;">
		<Logo/>
		<LineBreakMiniTransitMap
			lineColour="var(--brandYellow)"
			dotFill="var(--brandYellow)"
			dotStoke="var(--brandWhite)"
		/>
	</div>
	
	<TitleStandard
		title="Measuring the social inclusion benefits of transit oriented communities"
		subtitle="Via mapping data on activity participation in the Toronto region"
	/>

	<div class="text">

		<AuthorDate
			authors="<a href='' target='_blank'>Author Name</a> <a href='' target='_blank'>Author Name</a> & <a href='' target='_blank'>Author Name</a>"
			date="November 2025"
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
		<p>
			A core function of urban transportation is to help people take part in everyday life—such as getting to work, school, shopping, or socializing. Yet work in transportation planning, and particularly on assessing impacts of new public transit and transit-oriented development, has mostly focused on metrics like reduction in travel times, congestion, and emissions, as well as financial impacts, among others. 
		</p>
		<p>	
			While these are important, they often overlook or don't directly answer a key question: do living next to transit, and in transit-oriented communities, actually help everyone get to where they want to go on a daily basis? 
		</p>
		<p>	
			If there are limited transportation options, it can cause risks of social exclusion, which can broadly be defined as inability participate in society (link to a couple Steve papers here).
		</p>
	</div>

	<!-- IMAGE SCHEMATIC Transport Social Exclusion -->

	<div class="text">
		<p>
			<a href="https://doi.org/10.1016/j.trd.2019.102212">We wrote a paper a few years ago</a> that explored how increased transit accessibility to destinations improves people’s ability to participate in everyday life in the Greater Toronto and Hamilton Area (GTHA). A core finding of this work is that low-income and car-free households in areas with low transit accessibility were the most affected, lack of quality public transit options were limiting their ability to travel to places and participate in society. 
		</p>
		<p>
			On this page, we update some of this analysis with more recent data and specifically look at the social inclusion benefits that specifically living near major rail transit stations can have.
		</p>
		<p>
			We do this via measuring <span style="color:var(--brandDarkBlue);"><b>activity participation</b></span>, a metric which refers to how often people can take part in everyday activities. It can be directly quantified from travel survey data by simply counting of how many activities, or destinations, that someone visits per day. 
		</p>
	</div>

	<GraphicSingle
		svg720={"./activity-participation/activity-schematic-720.svg"}
		svg360={"./activity-participation/activity-schematic-360.svg"}
	/>

	<div class="text">
		<p>
			For our analysis, we used the Transportation Tomorrow Survey (TTS) to estimate activity participation for residents Greater Toronto Area. (The survey is a 5% sample of all households). 
		</p>
		<p>
			On average, we find that people travel to and partake in 1.15 activities per day. 
		</p>
		<p>
			Of course there will be idiosyncratic variations at an individual level, but by aggregating and looking at averages across different socio-economic groups or between neighbourhoords, it can reveal stark differences.
		</p>
		<p>	
			For example, those in households with higher incomes, on average, participate in more activities. This is particularly residents who are low income and also do not have regular access to a car. People who are in households that do not own or lease a car, and are low-income (less than $60k per year), have an average daily activity participation rate 0.89, 22% less than the overall population.
		</p>
	</div>

	<div class="text">
		<p>
			We can also map activity participation by neighbourhood. The map below shows in red areas with very low average activity participation, less than 1 activity per day per person. Certain inner- and outer-suburban areas appear to be the lowest: Scarborough, northern Etobicoke, swaths of Markham, Brampton, and Mississauga. Many of these neighbourhoods are also lower-income and home to recent immigrants.
		</p>
	</div>

	<GraphicSingle
		svg1080={"./activity-participation/activity-participation-map-1080.svg"}
		svg720={"./activity-participation/activity-participation-map-720.svg"}
	/>


	<div class="text">
		<p>
			But what role does living near a major transit station play? One notable pattern on the map is that central parts of Toronto have very few low participation neighbourhoods, even though a number of these are also home to many low-income residents who don't own cars. 
		</p>
		<p>
			Let's take a deeper look at this, by estimating average participation rates near (within 800m) and not near GO and TTC Subway stations.
		</p>
	</div>

	<!-- CHART - YES NO NEAR TRANSIT FOR ALL AND FOR LOW INC/NO CAR GROUP -->

	<!-- 
	=== Activities_mean weighted by persons_5up ===
	Population inside buffer: 940027
	Weighted mean inside buffer: 1.2023 ± 0.0012
	Population outside buffer: 5344517
	Weighted mean outside buffer: 1.1388 ± 0.0005

	=== Activities_mean_nocar_lowinc weighted by person_ind_low_income_no_car_hhld ===
	Population inside buffer: 84863
	Weighted mean inside buffer: 1.0098 ± 0.0052
	Population outside buffer: 175865
	Weighted mean outside buffer: 0.8362 ± 0.0036 
	-->

	<div class="text">
		<p>
			Clearly living near a public transit station has benefits for enabling residents to travel to and participate in daily activities, especially for low-income residents who do not have a car. But what about the characteristics of those stations? Some stations have better connections to other parts of the city. Some stations have better mixed-use development that enables local trips (e.g. shopping) without having to rely on a car.
		</p>
	</div>

	<!-- CHART - SHOW DIFFERENCE BY LOWINC NO CAR BY WHAT? GO vs TTC? BY TRANSIT LINE? BY MUNICIPALITY? -->

	               <!-- line_name    population  weighted_mean    moe_95
0                               ALL   1518.779835       1.092521  0.014390
1                            Barrie    260.510700       0.534216  0.013754
2                         Kitchener   3932.227900       0.885277  0.020741
3                    Lakeshore East   3995.123561       0.872319  0.043705
4                    Lakeshore West   3061.677946       1.039200  0.010163
5   Line 1: Yonge-University Subway  46758.174575       1.081490  0.005776
6     Line 2: Bloor-Danforth Subway  37514.019062       1.052038  0.007930
7           Line 4: Sheppard Subway   4283.328102       0.801947  0.019787
8                            Milton   2100.842509       0.959785  0.028004
9                     Niagara Falls           NaN            NaN       NaN
10                    Richmond Hill   1113.182734       0.426946  0.039683
11                      Stouffville   2815.885519       0.690343  0.038593 -->

	<div class="text">
		<p>
			Stations on the TTC Subway lines have higher participation rates than GO Rail stations. This is likely because TTC Subway routes provide connections to many neighbourhoods are much less commuter-focused than GO Rail. As well, many TTC Subway stations are located in walkable neighbourhoods with greater sets of amenities. Conversely, most GO Rail stations were built on historic rail corridors, which have a backdrop of more industrial land-uses, and many are currently surrounded by surface parking lots promoting park-and-ride trips, rather than mixed-use neighbourhoods that would encourage trips by active travel modes.
		</p>
	</div>

	<!-- PHOTOS? OR MAPS? of TOP AND BOTTOM STATIONS (WHERE N IS HIGH ENOUGH) -->

	<div class="text">
		<p>
			Next steps?
			- correlate station level activity participation with amenity density and/or access to destinations
			- multivariate analysis (ind. models) to parse out specific impacts of transit oriented development and communities that enable activity participation.
			- analysis in other cities where data is available
			- analyze participation in different types of activities
		</p>
	</div>

	<!-- <Footer /> -->

</main>
