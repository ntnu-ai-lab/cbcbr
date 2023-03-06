package no.ntnu.mycbr.rest.controller;

import java.util.*;

import no.ntnu.mycbr.core.ICaseBase;
import no.ntnu.mycbr.core.Project;
import no.ntnu.mycbr.core.casebase.Instance;
import no.ntnu.mycbr.core.model.Concept;
import io.swagger.annotations.ApiOperation;
import no.ntnu.mycbr.rest.App;
import no.ntnu.mycbr.rest.common.ApiResponseAnnotations.ApiResponsesDefault;
import no.ntnu.mycbr.rest.controller.helper.Case;
import no.ntnu.mycbr.rest.controller.helper.Query;
import no.ntnu.mycbr.rest.controller.service.CaseService;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import no.ntnu.mycbr.core.model.AttributeDesc;
import no.ntnu.mycbr.core.casebase.Attribute;
import no.ntnu.mycbr.core.DefaultCaseBase;
import static no.ntnu.mycbr.rest.utils.QueryUtils.getFullResult;

import static no.ntnu.mycbr.rest.common.ApiResponseAnnotations.*;
import static no.ntnu.mycbr.rest.common.ApiPathConstants.*;
import static no.ntnu.mycbr.rest.common.ApiOperationConstants.*;

@RestController
public class CaseController
{
    private static final String CASES_BY_PATTERN = "/casesByPattern";

    @Autowired
    private CaseService instanceService;

    private final Log logger = LogFactory.getLog(getClass());

    //Get one instance
    @ApiOperation(value = GET_CASE_BY_CASE_ID, nickname = GET_CASE_BY_CASE_ID)
    @RequestMapping(method = RequestMethod.GET, value = PATH_CONCEPT_CASEBASE_CASE_ID, 
    headers=ACCEPT_APPLICATION_JSON)
    @ApiResponsesDefault
    public Map<String, String> getInstance(
	    @PathVariable(value=CONCEPT_ID) String conceptID,
	    @PathVariable(value=CASEBASE_ID) String casebaseID,
	    @PathVariable(value=CASE_ID) String caseID) {

	Project p = App.getProject();
	
	if (!p.getCaseBases().containsKey(casebaseID))
	    return null;

	Instance instance = p.getInstance(caseID);
	
	Case queriedCase = new Case(instance.getName(),conceptID); 
	
	return queriedCase.getCase();
    }

    //Delete one instance
    @ApiOperation(value = DELETE_CASE_BY_CASE_ID, nickname = DELETE_CASE_BY_CASE_ID)
    @RequestMapping(method = RequestMethod.DELETE, value = PATH_CONCEPT_CASEBASE_CASE_ID, 
    headers=ACCEPT_APPLICATION_JSON)
    @ApiResponsesDefault
    public boolean deleteInstance(
	    @PathVariable(value=CONCEPT_ID) String conceptID,
	    @PathVariable(value=CASEBASE_ID) String casebaseID,
	    @PathVariable(value=CASE_ID) String caseID) {
	Project p = App.getProject();
	if(!p.getCaseBases().containsKey(casebaseID))
	    return false;
	ICaseBase cb = p.getCaseBases().get(casebaseID);
	if(cb.containsCase(casebaseID)==null)
	    return false;
	p.getCaseBases().get(casebaseID).removeCase(caseID);
	return true;
    }

    // Get all instances in case base of a concept
    @ApiOperation(value = GET_ALL_CASES, nickname = GET_ALL_CASES)
    @RequestMapping(method = RequestMethod.GET, value = PATH_CONCEPT_CASES, headers=ACCEPT_APPLICATION_JSON)
    @ApiResponsesDefault
    public List<Map<String, String>> getAllInstances(
	    @PathVariable(value=CONCEPT_ID) String conceptID) {
	
	Project p = App.getProject();

	/*Query query = new Query(conceptID);

        System.out.println("p get all instances size: "+p.getAllInstances().size());
        //System.out.println("is getallcases"+App.getProject().getSuperConcept().getAllInstances().size());
        //System.out.println("is getallcases"+App.getProject().getSuperConcept().getAllInstances().size());
        List<Instance> instances = new ArrayList<>();
        for(ICaseBase iCaseBase : p.getCaseBases().values()){
            logger.info("casebase has "+iCaseBase.getCases().size()+" cases ");
            instances.addAll(iCaseBase.getCases());
        }*/
	Collection<Instance> instances = p.getAllInstances();
	List<Map<String, String>> ret = new LinkedList<>();
	for(Instance instance : instances){
	    if(instance.getConcept().getName().contentEquals(conceptID))
		ret.add(new Case(instance.getName(),conceptID).getCase());
	}
	return ret;
    }

    // Get all instances of a concept
    @ApiOperation(value = GET_ALL_CASES_FROM_CASEBASE, nickname = GET_ALL_CASES_FROM_CASEBASE)
    @RequestMapping(method = RequestMethod.GET, value = PATH_CONCEPT_CASEBASE_CASES, 
    headers=ACCEPT_APPLICATION_JSON)
    @ApiResponsesDefault
    public List<LinkedHashMap<String, String>> getAllInstancesInCaseBase(
	    @PathVariable(value=CONCEPT_ID) String conceptID,
	    @PathVariable(value=CASEBASE_ID) String casebaseID) {
	
	Query query = new Query(casebaseID,conceptID);
	//TODO: filter to one type of concept
	List<LinkedHashMap<String, String>> cases = getFullResult(query, conceptID);
	return cases;
    }


    //Delete all instances
    @ApiOperation(value=DELETE_ALL_CASES, nickname=DELETE_ALL_CASES)
    @RequestMapping(method=RequestMethod.DELETE, value = PATH_CONCEPT_CASEBASE_CASES)
    @ApiResponsesDefault
    public boolean deleteInstances(
	    @PathVariable(value=CONCEPT_ID) String conceptID,
	    @PathVariable(value=CASEBASE_ID) String casebaseID) throws Exception {

	Project p = App.getProject();
	if(!p.getCaseBases().containsKey(casebaseID))
	    return false;
	//Collection<Instance> collection = p.getCaseBases().get(casebaseID).getCases();
	//collection.removeAll(p.getCaseBases().get(casebaseID).getCases());
	//p.getCaseBases().get(casebaseID).removeCase();
	//collection.clear();
	//(p.getCaseBases().get("CB_csvImport")).removeCase("43000");
	//Instance contains=(p.getCaseBases().get("CB_csvImport")).containsCase("KP41822");
	//if(contains!=null)
//		throw new Exception(contains.toString());
//Collection<Instance> collection2=p.getCaseBases().get(casebaseID).getCases();
//collection2.clear();
DefaultCaseBase cb=(DefaultCaseBase)(p.getCaseBases().get(casebaseID));


//cb.clearCases();

//int ii=0;
//	for(Iterator<Instance> iterator=collection.iterator();iterator.hasNext();){
//		Instance i=iterator.next();
	   // iterator.remove();
		//cb.addCase(i);
		
		//p.getCaseBases().get(casebaseID).removeCase(i.getName());
	//	p.removeCase(i.getName());
	//	i.cleanUp();
	//	cb.removeCase(i.getName());
	//	i=null;
		//HashMap<AttributeDesc, Attribute> map=i.getAttributes();
		//Iterator<AttributeDesc>  it = map.keySet().iterator();
	//	for (Iterator<AttributeDesc>  it = map.keySet().iterator();it.hasNext();)
	//	{
	//	AttributeDesc item = it.next();
	//		it.remove();
		   
		 //  i.removeAttribute(item);
		//   item=null;
		   //map.remove(item.getKey());
		//}
		//for (AttributeDesc value : map.keySet()) {
		//i.removeAttribute(value);
		//}
	//	ii++;
//	}
	//(p.getCaseBases().get(casebaseID).getCases()).clear();
	//collection=p.getCaseBases().get(casebaseID).getCases();
//	Collection<Instance> stances= ((Concept)p.getSubConcepts().get(conceptID)).getDirectInstances();
//	for(Iterator<Instance> iterator=stances.iterator();iterator.hasNext();){
//		Instance i=iterator.next();
//	    iterator.remove();
//	}
	//cb.clearCases();
	((Concept)p.getSubConcepts().get(conceptID)).removeAllDirectInstances(cb);
	//p.removeAllDirectInstances();
	//((Concept)p.getSubConcepts().get(conceptID)).update(null,null);
	//p.save();
	//Collection<Instance> instances = p.getAllInstances();
	//if(ii==0)
		//throw new Exception(Integer.toString(ii)+" "+Integer.toString(collection.size())+" "+Integer.toString(instances.size()));
			//p.removeCase("KP41822");
	//p.deleteCaseBase("CB_csvImport");
	//p.createDefaultCB("CB_csvImport");
	return true;
    }


    //Delete instances according to pattern
    @ApiOperation(value=DELETE_ALL_CASES_IN_CASEBASE_USING_PATTERN, nickname=DELETE_ALL_CASES_IN_CASEBASE_USING_PATTERN)
    @RequestMapping(method=RequestMethod.DELETE, value = PATH_CONCEPT_CASEBASE_CASES + CASES_BY_PATTERN)
    @ApiResponsesDefault
    public boolean deleteInstancePattern(
	    @PathVariable(value=CONCEPT_ID) String conceptID,
	    @PathVariable(value=CASEBASE_ID) String caseBase,
	    @RequestParam(value="pattern",defaultValue="*") String pattern) {

	Project p = App.getProject();
	if(!p.getCaseBases().containsKey(caseBase))
	    return false;
	if(pattern.contentEquals("*")){//this means delete all
	    Collection<Instance> collection = p.getCaseBases().get(caseBase).getCases();
	    Iterator<Instance> it = collection.iterator();
	    while(it.hasNext()){
		p.removeCase(it.next().getName());
	    }
	    p.save();
	}else{
	    Collection<Instance> collection = p.getCaseBases().get(caseBase).getCases();
	    for(Instance i : collection){
		collection.remove(i);
	    }

	}
	return true;
    }

    /*
    Add instances
    input should be:
    {cases:
    [
    {id:"caseid0",otherattribute:value,..}
    {id:"caseid1",otherattribute:value,..}
    ]
    }
     */
    @ApiOperation(value = ADD_MULTIPLE_CASES_USING_JSON, nickname = ADD_MULTIPLE_CASES_USING_JSON)
    @RequestMapping(method = RequestMethod.POST, value = PATH_CONCEPT_CASEBASE_CASES, 
    headers=ACCEPT_APPLICATION_JSON)
    @ApiResponsesDefault
    public ArrayList<String> addInstancesJSON(
	    @PathVariable(value=CONCEPT_ID) String conceptID,
	    @PathVariable(value=CASEBASE_ID) String casebaseID,
	    @RequestBody(required= true) JSONObject json) throws Exception {

	Project p = App.getProject();
	if(!p.getCaseBases().containsKey(casebaseID)){
	    return new ArrayList<>();
	}
	Concept c = (Concept)p.getSubConcepts().get(conceptID);
	ArrayList arr=new ArrayList((ArrayList) json.get(CASES));
JSONArray newCasess = new JSONArray();
newCasess.addAll(arr);
	//JSONArray newCases = (JSONArray) json.get(CASES);
	if(c.getAttributeDesc("ControlPointText").isMultiple())
		c.getAttributeDesc("ControlPointText").setMultiple(false);
		

	ArrayList<String> retttt= instanceService.addInstances(c,casebaseID, newCasess);
	return retttt;
    }

    @ApiOperation(value = ADD_CASE_USING_JSON, nickname = ADD_CASE_USING_JSON)
    @RequestMapping(method = RequestMethod.PUT, value = PATH_CONCEPT_CASEBASE_CASE_ID, 
    headers=ACCEPT_APPLICATION_JSON)
    @ApiResponsesDefault
    public boolean addInstanceJSON(
	    @PathVariable(value=CONCEPT_ID) String conceptID,
	    @PathVariable(value=CASEBASE_ID) String casebaseID,
	    @PathVariable(value=CASE_ID) String caseID,
	    @RequestBody(required= true) JSONObject json) {
	
	Project p = App.getProject();
	if(!p.getCaseBases().containsKey(casebaseID)){
	    return false;
	}
	ICaseBase cb = p.getCaseBases().get(casebaseID);
	Concept c = (Concept)p.getSubConcepts().get(conceptID);
	
	return null != instanceService.addInstance(c, cb, caseID, json);
    }
}
