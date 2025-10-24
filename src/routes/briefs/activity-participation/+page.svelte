<script>

	import '../../../assets/global-styles.css';

	import Logo from '$lib/LogoBody.svelte';
	import TitleFullPage from '$lib/TitleFullPage.svelte';
	import TitleHalfSplit from '$lib/TitleHalfSplit.svelte';
	import TitleStandard from '$lib/TitleStandard.svelte';
	import AuthorDate from '$lib/AuthorDate.svelte';
	import ImageSingle from '$lib/ImageSingle.svelte';
	import GraphicSingle from '$lib/GraphicSingle.svelte';
	import GraphicsMultiples from '$lib/GraphicMultiples.svelte';
	import Footer from '$lib/Footer.svelte';
	import ScrollyImages from "$lib/ScrollyImages.svelte";
	
	
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

	<div class="text" style="margin-top: 150px; margin-bottom: 20px; border-bottom: solid 1px var(--brandLightBlue);">
		<Logo/>
	</div>
	

	
	<TitleStandard
		title="Measuring the social inclusion benefits of transit oriented communities"
		subtitle="Via mapping data on activity participation in the Toronto region"
	/>

	<div class="text">

		<AuthorDate
			authors="<a href='' target='_blank'>Author Name</a> & <a href='' target='_blank'>Author Name</a>"
			date="November 2025"
		/>

	</div>

	<ImageSingle
		imageURL="https://jamaps.github.io/photos/picimgs/taipei1_2025.jpg"
		caption="Taipei skyline."
		source="Jeff Allen."
		altText=""
		maxWidth="680px"
	/>

	<div class="text">
		<p>
			A core function of urban transportation is to help people take part in everyday life—like getting to work, school, shopping, or visiting friends. Work in transportation planning, and particularly on assessing impacts of new public transit, has mostly focused on metrics like reducing travel times, congestion, and pollution, as well as financial impacts, among others. While these are important, they often overlook a key question: does the system actually help everyone get where they want to go. If there are limited transportation options, it can lead to social exclusion, inability participate in society.
		</p>
	</div>
 
	<!-- IMAGE SCHEMATIC Transport Social Exclusion -->

	<div class="text">
		<p>
			A few years ago, we wrote a paper that explores how increased public transit accessibility improves people’s ability to participate in everyday life in the Greater Toronto and Hamilton Area (GTHA). A core finding of this work is that low-income and car-free households in areas with low transit accessibility were the most affected, lack of quality public transit options were limiting their ability to travel to places and participate in society. On this page, we update some of this analysis with more recent data and specifically look at the social inclusion benefits that living near major rail transit lines can have.
		</p>
		<p>
			Activity participation refers to how often people can take part in everyday activities—like going to work or school, shopping, attending appointments, or socializing. This can be quantified from travel survey data by simply counting of how many places, or 'activities' that someone visits per day. 
		</p>
	</div>

	<!-- IMAGE SCHEMATIC  -->

	<div class="text">
		<p>
			The Transportation Tomorrow Survey (TTS) is the largest travel survey and covers the Greater Golden Horseshoe. The survey includes a 'diary' of where people travel and what the purpose of their trip is (work, school, shopping, etc.). For each person in this survey, we counted their total number of activities. Of course there will be  variations, but by aggregating and looking at averages across different socio-economic groups or between neighbourhoords, it can reveal stark differences. For example, those in households with higher incomes, on average, participate in more activities. Particularly residents who are low income and do not have a motor vehicle. Cars are increasingly expensive, ... , ____. age, immigration, etc. 
		</p>
	</div>

	<div class="text">
		<p>
			We can also map activity participation by neighbourhood. Low areas, which can be called <i>participation desserts</i>, are those with are facing ____ social exclusion?. The map below shows in red areas with low average activity participation, less than 1 activity per day. Inner and outer suburban areas appear to be the lowest: Scarborough, northern Etobicoke, swaths of Markham, Brampton, and Mississauga. Many of these neighbourhoods are also lower-income and _____. 
		</p>
	</div>

	<!-- MAP - ACTIVITY PARTICIPATION SURFACE + MAJOR TRANSIT -->

	<div class="text">
		<p>
			But what role does living near a major transit station play? One notable pattern on the map is that central parts of Toronto have very few low participation neighbourhoods, even though many of these are also are home to many low-income residents. Let's take a look at this a bit further, by estimating average participation rates near (with 800m) and not near GO and TTC Subway stations.
		</p>
	</div>

	<!-- CHART - YES NO NEAR TRANSIT FOR ALL AND FOR LOW INC/NO CAR GROUP -->

	<div class="text">

		<p>
			Describe results
		</p>
		
		<p>
			Qualities of a TOC, connectivity to the city, to employment, to school and education. But also to the development around the transit station - are there grocery stores you can walk to - is there a daycare, is there a library. In more suburban areas, if you live near a transit station that you can access Downtown reasonably well to go to work, but not other amenities, it may be harder to do things locally.
		</p>
		
	</div>

	<!-- CHART - SHOW DIFFERENCE BY LOWINC NO CAR BY WHAT? GO vs TTC? BY TRANSIT LINE? BY MUNICIPALITY? -->

	<div class="text">

		<p>
			What our paper showed, limitations. Possible research directions individual models benefits of types of TOD. This meant as mostly descriptive. Types of activities.
		</p>

	</div>


	<div class="text">

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

	

	<div class="text">

		<Footnotes footnotes={footnotes} />
		
	</div>

	<Footer />

</main>