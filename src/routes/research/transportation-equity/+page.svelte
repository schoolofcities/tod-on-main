<script>

	import '../../../assets/global-styles.css';

	import Logo from '$lib/LogoBody.svelte';
	import TitleVideo from '$lib/TitleVideo.svelte';
    import TitlePage from '$lib/TitlePage.svelte';
	import AuthorDate from '$lib/AuthorDate.svelte';
	import ImageSingle from '$lib/ImageSingle.svelte';
	import GraphicSingle from '$lib/GraphicSingle.svelte';
	import GraphicsMultiples from '$lib/GraphicMultiples.svelte';
	import Footer from '$lib/Footer.svelte';
	import ScrollyImages from "$lib/ScrollyImages.svelte";
	import LineBreakMiniTransitMap from '$lib/LineBreakMiniTransitMap.svelte';
	import Password from '$lib/Password.svelte';
	
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

	<title>TOD Research - Transportation Equity | School of Cities</title>

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

	<Password correctPassword="meowmeowcat"></Password>

	<!-- <TitleVideo
		title="Transportation equity and sustainable mobility from mixed-use development"
		subtitle=""
		titletype="RESEARCH"
		video="/tod-on-main/research/embodied-carbon/skylineVideo.mp4"
		videoSpeed={0.67}
		videoOpacity={0.8}
		titleFontColour="var(--brandWhite)"
		subtitleFontColour="var(--brandWhite)"
		logoType = 'White';
	/> -->
	<TitlePage
		title="Transportation equity and sustainable mobility from mixed-use development"
		type="Research"
		bgType="Video"
		url="/tod-canada/web-assets/research/embodied-carbon/skylineVideo.mp4"
		videoSpeed={0.67}
		videoOpacity={0.8}
		titleFontColour="var(--brandWhite)"
		subtitleFontColour="var(--brandWhite)"
		logoType = 'White';
	/>


	<div class="text">

		<AuthorDate
			authors="<a href='' target='_blank'>Author Name</a> <a href='' target='_blank'>Author Name</a> & <a href='' target='_blank'>Author Name</a>"
			date="April 2026 (do we include a date?)"
		/>

	</div>

	

	<div class="text">
		<h1>
			Why does this matter?
		</h1>
		<p>
			New developments, including changes to land use, population, and employment patterns, influence how people travel and alter the distribution of transportation-related advantages and disadvantages. This study measures how transit-oriented development (TOD) affects two important metrics: transportation equity and sustainable mode shift.  
		</p>
		<p>	
			<span class="highlight" style="background-color: #F1C500; color: black;opacity: 0.8;">Transportation equity</span> asks who gains access to mobility and opportunity, who faces costs or constraints, and what the magnitudes of those impacts are.1 
		</p>
		<p>	
			<span class="highlight" style="background-color: #F1C500; color: black;opacity: 0.8;">Mode shift</span> evaluates how development patterns influence sustainable transportation outcomes by looking at the percentage of people who switch from driving to more sustainable modes of travel, such as transit, walking, or cycling. 
		</p>
		<p>	
			By projecting how a development may reshape where people live and work, we can assess how different scenarios will reduce or exacerbate transportation disadvantage and sustainability. 
		</p>

		
		<h1>
			Methodology
		</h1>
		<p>
			Our focus in measuring transportation equity was on understanding how people living in poverty, as defined by Statistics Canada’s Low Income Cut-Off threshold, could access employment opportunities under different development scenarios. To assess the potential impact of different types of TOD, we implemented Foster-Greer-Thorbecke Indices, which quantify how over-represented low-income households are in areas of transport disadvantage.2 
		</p>
		<p>	
			We began by assessing <span class="highlight" style="background-color: #AB1368; color: white;opacity: 0.8;">current conditions</span>, using census data for low-income households and business register data for employment, to calculate baseline accessibility scores at the dissemination area level. We then created three development scenarios: 
		</p>

		<ul>
			<li>
				A <span class="highlight" style="background-color: #007894; color: white;opacity: 0.8;">current trajectory</span>, which follows existing growth patterns within the TOD 
			</li>
			<li>
				A <span class="highlight" style="background-color: #00A189; color: white;opacity: 0.8;">optimized scenario</span>, which uses more optimal land use changes within the TOD 
			</li>
			<li>	
				A <span class="highlight" style="background-color: #6D247A; color: white;opacity: 0.8;">general growth scenario</span> which assumes the same population and job growth as in the current trajectory but distributes it across the municipalities3 rather than concentrating it in the station area, in proportion to their existing values 
			</li>
		</ul>

		<p>
			To evaluate sustainable mode shift, we used trip generation analysis to estimate the number and types of trips associated with the current trajectory and optimized development scenarios above, compared to existing conditions. Here we apply the Mixed-Use District Travel Model from Envision Tomorrow because the industry standard model for measuring trip generation uses estimates that are largely based on suburban locations with limited pedestrian or transit infrastructure, making it less suitable for mixed-use and transit-oriented developments.4 From this model, we selected the variables most affected by TOD, namely population, employment, land use, and residential dwelling mix5￼ ￼as well as two outcome variables for each scenario:  
		</p>

		<ul>
			<li>
				<strong>Sustainable mode share:</strong> the percentage of trips made by sustainable modes 
			</li>
			<li>
				<strong>Sustainable mode shift:</strong> the increase in sustainable mode share from the baseline scenario to the new scenario (e.g. a 10% rise in walking trips) 
			</li>
			
		</ul>

		<p>
			Click here for a more detailed discussion of the methodology. 
		</p>

	</div>

	<!-- <GraphicSingle
		svg720={"../web-assets/research/transportation-equity/edmonton-access-example-720.svg"}
		svg360={"../web-assets/research/transportation-equity/poverty-scenario-360.svg"}
	/> -->

	<div class="text">

		<h1>
			Findings
		</h1>

		<h2>
			TOD increases transportation access and equity
		</h2>

		<p>
			Compared with a general growth scenario, densifying near transit increases equity by allowing more low-income households to access opportunities within their neighbourhoods and through the transit network. This finding was consistent across all of the sites studied. The depth of the impact is closely tied to the number of affordable units included in the development, so increasing the number of affordable units will amplify transportation equity benefits, extending this access to thousands more families. 
		</p>


	</div>

	<GraphicSingle
		svg720={"../web-assets/research/transportation-equity/poverty-scenario-720.svg"}
		svg360={"../web-assets/research/transportation-equity/poverty-scenario-360.svg"}
	/>

	<div class="text">

		<h2>
			TOD consistently enables a shift to more sustainable modes 
		</h2>

		<p>
			Across all case studies, new development in mixed-use districts reduces vehicle trips and increases transit and walking trips for both internal and external travel. These shifts reflect the combined effects of increasing the diversity of land uses, shorter trip distances, and improved access to non-auto modes within station areas. While the direction of change is consistent, the magnitude of the sustainable mode shift and final mode share varies across the case studies, reflecting differences in local context, scale, and network connectivity.  
		</p>

	</div>

	<GraphicSingle
		svg720={"../web-assets/research/transportation-equity/mode-shift-720.svg"}
		svg360={"../web-assets/research/transportation-equity/mode-shift-360.svg"}
	/>

	<div class="text">

		<h2>
			Transit improvements should be directed to larger station areas with limited existing access
		</h2>

		<p>
			Larger station areas – those with more people and jobs – show higher absolute sustainable mode shares following new development, which reflects broader urban patterns showing that people tend to walk and take transit more in larger, denser cities. Yet the sustainable mode shift in these areas is proportionally lower, with the largest station areas showing only modest increases. In these areas, significant shifts in sustainable mode share cannot be achieved by development in a single mixed-use district: these areas are already well served, so increased development with existing service shows only marginal returns.   
		</p>

		<p>
			However, cities can see greater sustainable mode shifts by increasing transit investment in these areas, which can connect them with a greater number of jobs in the region. Planned investments such as the Hurontario LRT in Cooksville may therefore have a significant impact on converting external vehicle trips into transit trips. Larger station areas that can better connect into existing or planned higher-order transit networks are better positioned to realize meaningful mode share gains. 
		</p>

	</div>


</main>
