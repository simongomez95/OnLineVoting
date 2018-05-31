package identifier.Controller;

import identifier.Logic.IdentifierService;
import identifier.Repository.Entities.Identifier;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import java.util.Optional;


@Controller
public class IdentifierController {

    @Autowired
    IdentifierService idService;

    @RequestMapping(value = "/generateId", method = RequestMethod.POST)
    public ResponseEntity<?> generateId(@RequestBody Identifier pair) {

        if (pair == null  || StringUtils.isEmpty(pair.getNonce())){
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }

        Optional<Identifier> newId = idService.saveNonce(pair);

        if (newId.isPresent()) {
            return new ResponseEntity<>(newId.get(), HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }
    }

    @RequestMapping(value = "/getNonce", method = RequestMethod.POST)
    public ResponseEntity<?> getNonce(@RequestBody Identifier pair) {

        if (pair == null  || pair.getId() == null){
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }
        long id = pair.getId();
        Optional<Identifier> newId = idService.getNonce(id);

        if (newId.isPresent()) {
            return new ResponseEntity<>(newId.get(), HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }
    }
}
