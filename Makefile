TARGETS=radio program_name download_image autorecorder

all: $(TARGETS)

$(TARGETS): %:%.src
	./compile.py $< $@

rebuild: clean all

run: $(TARGETS)
	./autorecorder minimax | tee log

clean:
	rm -f *~
	rm -f $(TARGETS)
